#!/usr/bin/env python3
"""
A module for taking a list of ints and returning their sum as floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    function that takes list of ints and returns their sum as floats
    """
    return sum(mxd_lst)
