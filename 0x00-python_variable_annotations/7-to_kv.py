#!/usr/bin/env python3
"""
Module for generating a list of all possible combinations
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair into a tuple of string and float
    """
    return (k, float(v ** 2))
