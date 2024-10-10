#!/usr/bin/env python3
"""
A mofule for working with Any, Mapping, TypeVar, Union in typing
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Safely gets a value from a dictionary and returns key-value
    if present and default if not
    """
    if key in dct:
        return dct[key]
    else:
        return default
