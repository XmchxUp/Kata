"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""


def foo(**kwargs: int | str):
    ...


foo(a=1, bar="2")
foo(a=[1])
