from quik.base import QuikNamespace


class QuikCalcNamespace(QuikNamespace):
    def calc_buy_sell(self, class_code, sec_code, client_code, account, price, is_buy, is_market):
        return self.quik.invoke("CalcBuySell", class_code, sec_code, client_code, account, price, is_buy, is_market)

    def buy_market(self, class_code, sec_code, client_code, account):
        return self.calc_buy_sell(class_code, sec_code, class_code, account, 0.0, True, True)

    def sell_market(self, class_code, sec_code, client_code, account):
        return self.calc_buy_sell(class_code, sec_code, class_code, account, 0.0, False, True)

    def buy_limit(self, class_code, sec_code, client_code, account, price):
        return self.calc_buy_sell(class_code, sec_code, class_code, account, price, True, False)

    def sell_limit(self, class_code, sec_code, client_code, account, price):
        return self.calc_buy_sell(class_code, sec_code, class_code, account, price, False, False)