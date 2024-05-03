#!/usr/bin/env python3
"""
Module for safely retrieving a value from a dictionary with a default.

"""

from typing import Mapping, Any, TypeVar, Optional

# Type variable that could be any type or None
T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T], 
    key: Any, 
    default: Optional[T] = None
) -> Optional[T]:
    """
    Get the value from a dictionary by key or return a default value.

    """
    if key in dct:
        return dct[key]
    else:
        return default

