from quik.base import QuikNamespace


class QuikServiceNamespace(QuikNamespace):
    @property
    def script_path(self):
        return self.quik.invoke("getScriptPath")

    @property
    def working_folder(self):
        return self.quik.invoke("getWorkingFolder")

    @property
    def is_connected(self):
        return self.quik.invoke("isConnected") > 0

    @property
    def trade_date(self):
        return self.quik.invoke("getTradeDate")

    def message(self, message, icon_type=1):
        self.quik.invoke("message", message, icon_type)

    def debug(self, message):
        self.quik.invoke("PrintDbgStr", message)

