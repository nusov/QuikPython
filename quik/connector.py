from quik.namespaces.tables import QuikTableNamespace
from quik.namespaces.transactions import QuikTransactionsNamespace
from quik.namespaces.securities import QuikSecuritiesNamespace
from quik.namespaces.quotes import QuikQuotesNamespace
from quik.namespaces.info import QuikInfoNamespace
from quik.namespaces.service import QuikServiceNamespace
from quik.namespaces.lua import QuikLuaNamespace
from quik.namespaces.calc import QuikCalcNamespace
from quik.namespaces.ticks import QuikTicksNamespace


class QuikConnector(object):
    def __init__(self, quik):
        self.tables = QuikTableNamespace(quik)
        self.transactions = QuikTransactionsNamespace(quik)
        self.securities = QuikSecuritiesNamespace(quik)
        self.quotes = QuikQuotesNamespace(quik)
        self.info = QuikInfoNamespace(quik)
        self.service = QuikServiceNamespace(quik)
        self.lua = QuikLuaNamespace(quik)
        self.calc = QuikCalcNamespace(quik)
        self.ticks = QuikTicksNamespace(quik)

