"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""

from typing import ClassVar


class Foo:
    """Hint: No need to write __init__"""

    bar: ClassVar[int]


Foo.bar = 1
Foo.bar = "1"
Foo().bar = "123"
