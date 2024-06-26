#!/usr/bin/env python3
"""
Module for safely retrieving a value from a dictionary with a default.

"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Get the value from a dictionary by key or return a default value.

    """
    if key in dct:
        return dct[key]
    else:
        return default
