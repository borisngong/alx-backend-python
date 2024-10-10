#!/usr/bin/env python3
"""
This module contains a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function returns a function that multiplies a float by multiplier
    """

    def multiply(value: float) -> float:
        return multiplier * value

    return multiply
