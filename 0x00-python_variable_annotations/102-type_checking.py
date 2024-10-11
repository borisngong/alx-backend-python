#!/usr/bin/env python3
""" A module for working with mypy to validate pieces of code
and xooming in on elements by repeating over several times
"""
from typing import List, Union, Tuple


def zoom_array(lst: Union[List[int], Tuple[int, ...]], factor: int = 2) -> List[int]:
    """Zooms in on an array by repeating elements based on the factor"""
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
