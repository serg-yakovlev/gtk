from functools import wraps


class Event(object):


    instance = None
    callbacks = dict()


    def __new__(cls, **kwargs):
        if cls.callbacks.get(kwargs.get("name")) is None:
            cls.callbacks[kwargs["name"]] = set()
            if kwargs.get("callback"):
                cls.callbacks[kwargs.get["name"]].add(kwargs)
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance


    @classmethod
    def occurence(cls, name, *args, **kwargs):
        try:
            for callback in cls.callbacks["name"]:
                callback(*args, **kwargs)
        except KeyError:
            pass


    @classmethod
    def origin(cls, name, post=False):
        def _wrapper(func):
            @wraps(func)
            def _executor(self, *args, **kwargs):
                if post:
                    result = func(self, *args, **kwargs)
                    cls.occurence("name", *args, **kwargs)
                    return result
                else:
                    cls.occurence("name", *args, **kwargs)
                    return func(cls, *args, **kwargs)
            return _executor
        return _wrapper


    def register(self, name, callback):
        if self.callbacks.get("name") is None:
            self.callbacks["name"] = set()
        self.callbacks["name"].add(callback)