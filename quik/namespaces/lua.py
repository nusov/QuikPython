from quik.base import QuikNamespace


class QuikLuaNamespace(QuikNamespace):
    def __getattr__(self, item):
        def wrapper(*args, **kwargs):
            return self.quik.invoke(item, *args)
        return wrapper
