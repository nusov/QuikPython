from quik.base import QuikNamespace


class QuikTicksNamespace(QuikNamespace):
    def pull(self, i):
        return self.quik.invoke("pull_trades", i)
