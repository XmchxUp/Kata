"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""

from typing import TypeVar

T = TypeVar("T", str, int)


def add(a: T, b: T) -> T:
    return a
