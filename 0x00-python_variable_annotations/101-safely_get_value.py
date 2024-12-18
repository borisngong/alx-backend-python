#!/usr/bin/env python3
"""
A module for working with Any, Mapping, TypeVar, Union in typing.
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Safely get a value from a dictionary with a default value."""
    if key in dct:
        return dct[key]
    else:
        return default
