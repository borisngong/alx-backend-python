#!/usr/bin/env python3
"""
A module that contain the function to calculate the mean of a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats

    Args:
        input_list (List[float]): A list of floats

    Returns:
        float: The sum of the floats in the list
    """
    return sum(input_list)
