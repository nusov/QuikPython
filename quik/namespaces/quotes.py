from quik.base import QuikNamespace


class QuikQuotesNamespace(QuikNamespace):
    def subscribe(self, class_code, sec_code):
        return self.quik.invoke("Subscribe_Level_II_Quotes", class_code, sec_code)

    def unsubscribe(self, class_code, sec_code):
        return self.quik.invoke("Unsubscribe_Level_II_Quotes", class_code, sec_code)

    def is_subscribed(self, class_code, sec_code):
        return self.quik.invoke("IsSubscribed_Level_II_Quotes", class_code, sec_code)

    def pull(self, class_code, sec_code):
        return self.quik.invoke("getQuoteLevel2", class_code, sec_code)