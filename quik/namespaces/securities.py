from quik.base import QuikNamespace, QuikNamespaceWithArg


class QuikSecuritiesNamespace(QuikNamespace):
    def get_classes(self):
        return filter(len, self.quik.invoke("getClassesList").split(","))

    def get_class_info(self, class_name):
        return self.quik.invoke("getClassInfo", class_name)

    def get_class_securities(self, class_name):
        return filter(len, self.quik.invoke("getClassSecurities", class_name).split(","))

    def get_security_info(self, class_name, sec_name):
        return self.quik.invoke("getSecurityInfo", class_name, sec_name)

