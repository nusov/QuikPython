from quik.base import QuikNamespace, QuikNamespaceWithArg


class QuikTable(QuikNamespaceWithArg):
    def __len__(self):
        return int(self.quik.invoke("getNumberOf", self.name))

    def __getitem__(self, index):
        r = self.quik.invoke("getItem", self.name, index)
        if r is None:
            raise IndexError
        return r


class QuikTableNamespace(QuikNamespace):
    @property
    def firms(self):
        return QuikTable(self.quik, "firms")

    @property
    def classes(self):
        return QuikTable(self.quik, "classes")

    @property
    def securities(self):
        return QuikTable(self.quik, "securities")

    @property
    def trade_accounts(self):
        return QuikTable(self.quik, "trade_accounts")

    @property
    def client_codes(self):
        return QuikTable(self.quik, "client_codes")

    @property
    def all_trades(self):
        return QuikTable(self.quik, "all_trades")

    @property
    def account_positions(self):
        return QuikTable(self.quik, "account_positions")

    @property
    def orders(self):
        return QuikTable(self.quik, "orders")

    @property
    def futures_client_holding(self):
        return QuikTable(self.quik, "futures_client_holding")

    @property
    def futures_client_limits(self):
        return QuikTable(self.quik, "futures_client_limits")

    @property
    def money_limits(self):
        return QuikTable(self.quik, "money_limits")

    @property
    def depo_limits(self):
        return QuikTable(self.quik, "depo_limits")

    @property
    def trades(self):
        return QuikTable(self.quik, "trades")

    @property
    def stop_orders(self):
        return QuikTable(self.quik, "stop_orders")

    @property
    def neg_deals(self):
        return QuikTable(self.quik, "neg_deals")

    @property
    def neg_trades(self):
        return QuikTable(self.quik, "neg_trades")

    @property
    def neg_deal_reports(self):
        return QuikTable(self.quik, "neg_deal_reports")

    @property
    def firm_holding(self):
        return QuikTable(self.quik, "firm_holding")

    @property
    def account_balance(self):
        return QuikTable(self.quik, "account_balance")

    @property
    def ccp_holdings(self):
        return QuikTable(self.quik, "ccp_holdings")

    @property
    def rm_holdings(self):
        return QuikTable(self.quik, "rm_holdings")
