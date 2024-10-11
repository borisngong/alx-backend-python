#!/usr/bin/env python3
"""
A module for working with Any, Mapping, TypeVar, Union in typing.
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """Safely gets a value from a dictionary and returns key-value
    if present and default if not"""
    if key in dct:
        return dct[key]
    else:
        return default
