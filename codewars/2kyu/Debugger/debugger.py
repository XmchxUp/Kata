from typing import Any


class Debugger(object):
    attribute_accesses = []
    method_calls = []


class Meta(type):
    # your solution
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                setattr(new_cls, attr_name, cls.wrap_method(attr_name, attr_value))
        new_cls.__getattribute__ = cls.wrap_getattribute(new_cls.__getattribute__)
        new_cls.__setattr__ = cls.wrap_setattr(new_cls.__setattr__)
        return new_cls

    @classmethod
    def wrap_method(cls, name, func):
        def wrapped(*args, **kwargs):
            Debugger.method_calls.append(
                {
                    "class": args[0].__class__,  # class object, not string
                    "method": name,  # method name, string
                    "args": args,  # all args, including self
                    "kwargs": kwargs,
                }
            )
            return func(*args, **kwargs)

        return wrapped

    @classmethod
    def wrap_getattribute(cls, func):
        def wrapped(self, name: str):
            if name != "__class__" and not name.startswith("__"):
                Debugger.attribute_accesses.append(
                    {
                        "action": "get",  # set/get
                        "class": self.__class__,  # class object, not string
                        "attribute": name,  # name of attribute, string
                        "value": None,  # actual value
                    }
                )
            return func(self, name)

        return wrapped

    @classmethod
    def wrap_setattr(cls, func):
        def wrapped(self, name: str, value: Any):
            if not name.startswith("__"):
                Debugger.attribute_accesses.append(
                    {
                        "action": "set",  # set/get
                        "class": self.__class__,  # class object, not string
                        "attribute": name,  # name of attribute, string
                        "value": value,  # actual value
                    }
                )
            return func(self, name, value)

        return wrapped


class Foo(object, metaclass=Meta):
    def __init__(self, x):
        self.x = x

    def bar(self, v):
        return (self.x, v)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        self._y = v

    @y.getter
    def y(self):
        return 10


f = Foo(1)

f.bar(1)
print(Debugger.method_calls)
print(Debugger.attribute_accesses)
f.y = 1
print(f.y)
