import zmq
import msgpack

from quik.exceptions import QuikInvokationException
from quik.exceptions import QuikTimeoutException


class QuikSocket(object):
    def __init__(self, uri, timeout=100):
        self.timeout = timeout
        self.zmq_ctx = zmq.Context()
        self.zmq_skt = self.zmq_ctx.socket(zmq.REQ)
        self.zmq_skt.setsockopt(zmq.LINGER, 0)
        self.zmq_pll = zmq.Poller()
        self.zmq_pll.register(self.zmq_skt, zmq.POLLIN)
        self.zmq_skt.connect(uri)

    def invoke(self, method, *args, override_timeout=None, **kwargs):
        self.zmq_skt.send(msgpack.packb([method.encode(), *args]))
        if self.zmq_pll.poll(override_timeout or self.timeout):
            s1, s2 = self.zmq_skt.recv_multipart()
            status = s1.decode()
            res = msgpack.unpackb(s2, encoding='cp1251')

            if status == 'OK':
                if len(res) > 1:
                    return tuple(res)
                elif len(res) == 1:
                    return res[0]
            else:
                raise QuikInvokationException(status)
        else:
            raise QuikTimeoutException
