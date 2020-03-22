class QuikNamespace(object):
    def __init__(self, quik):
        self.quik = quik


class QuikNamespaceWithArg(object):
    def __init__(self, quik, name):
        self.quik = quik
        self.name = name