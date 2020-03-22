from quik.base import QuikNamespace


class QuikInfoNamespace(QuikNamespace):
    @property
    def VERSION(self):
        return self.quik.invoke("getInfoParam", "VERSION")

    @property
    def TRADEDATE(self):
        return self.quik.invoke("getInfoParam", "TRADEDATE")

    @property
    def SERVERTIME(self):
        return self.quik.invoke("getInfoParam", "SERVERTIME")

    @property
    def LASTRECORDTIME(self):
        return self.quik.invoke("getInfoParam", "LASTRECORDTIME")

    @property
    def NUMRECORDS(self):
        return self.quik.invoke("getInfoParam", "NUMRECORDS")

    @property
    def LASTRECORD(self):
        return self.quik.invoke("getInfoParam", "LASTRECORD")

    @property
    def LATERECORD(self):
        return self.quik.invoke("getInfoParam", "LATERECORD")

    @property
    def CONNECTION(self):
        return self.quik.invoke("getInfoParam", "CONNECTION")

    @property
    def IPADDRESS(self):
        return self.quik.invoke("getInfoParam", "IPADDRESS")

    @property
    def IPPORT(self):
        return self.quik.invoke("getInfoParam", "IPPORT")

    @property
    def IPCOMMENT(self):
        return self.quik.invoke("getInfoParam", "IPCOMMENT")

    @property
    def SERVER(self):
        return self.quik.invoke("getInfoParam", "SERVER")

    @property
    def SESSIONID(self):
        return self.quik.invoke("getInfoParam", "SESSIONID")

    @property
    def USER(self):
        return self.quik.invoke("getInfoParam", "USER")

    @property
    def USERID(self):
        return self.quik.invoke("getInfoParam", "USERID")

    @property
    def ORG(self):
        return self.quik.invoke("getInfoParam", "ORG")

    @property
    def LOCALTIME(self):
        return self.quik.invoke("getInfoParam", "LOCALTIME")

    @property
    def CONNECTIONTIME(self):
        return self.quik.invoke("getInfoParam", "CONNECTIONTIME")

    @property
    def MESSAGESSENT(self):
        return self.quik.invoke("getInfoParam", "MESSAGESSENT")

    @property
    def ALLSENT(self):
        return self.quik.invoke("getInfoParam", "ALLSENT")

    @property
    def BYTESSENT(self):
        return self.quik.invoke("getInfoParam", "BYTESSENT")

    @property
    def BYTESPERSECSENT(self):
        return self.quik.invoke("getInfoParam", "BYTESPERSECSENT")

    @property
    def MESSAGESRECV(self):
        return self.quik.invoke("getInfoParam", "MESSAGESRECV")

    @property
    def BYTESRECV(self):
        return self.quik.invoke("getInfoParam", "BYTESRECV")

    @property
    def ALLRECV(self):
        return self.quik.invoke("getInfoParam", "ALLRECV")

    @property
    def BYTESPERSECRECV(self):
        return self.quik.invoke("getInfoParam", "BYTESPERSECRECV")

    @property
    def AVGSENT(self):
        return self.quik.invoke("getInfoParam", "AVGSENT")

    @property
    def AVGRECV(self):
        return self.quik.invoke("getInfoParam", "AVGRECV")

    @property
    def LASTPINGTIME(self):
        return self.quik.invoke("getInfoParam", "LASTPINGTIME")

    @property
    def LASTPINGDURATION(self):
        return self.quik.invoke("getInfoParam", "LASTPINGDURATION")

    @property
    def AVGPINGDURATION(self):
        return self.quik.invoke("getInfoParam", "AVGPINGDURATION")

    @property
    def MAXPINGTIME(self):
        return self.quik.invoke("getInfoParam", "MAXPINGTIME")

    @property
    def MAXPINGDURATION(self):
        return self.quik.invoke("getInfoParam", "MAXPINGDURATION")
