"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""

from typing import Final


my_list: Final = []


my_list.append(1)
my_list = []
my_list = "something else"
