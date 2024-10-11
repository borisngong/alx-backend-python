#!/usr/bin/env python3
""" A module for working with mypy to validate pieces of code
and xooming in on elements by repeating over several times
"""
from typing import List, Union


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    """
    Zoom in on an array by repeating each element a certain number of times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))  # Ensure factor is an integer
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
