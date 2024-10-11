#!/usr/bin/env python3
""" A module for working with mypy to validate pieces of code
and xooming in on elements by repeating over several times
"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on an array by repeating each element a certain number of times
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Convert to a tuple to match the function signature

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
