"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar

T = TypeVar("T", bound=Callable)


def decorator(func: T):
    return func
