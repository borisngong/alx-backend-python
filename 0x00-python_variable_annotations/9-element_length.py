#!/usr/bin/env python3
"""
A module for working with Iterable, Sequence, List, Tuple
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with each sequence and its length"""
    return [(i, len(i)) for i in lst]
