from quik.base import QuikNamespace


class QuikTransactionsNamespace(QuikNamespace):
    def send(self, tx):
        return self.quik.invoke("sendTransaction", tx)