#!/usr/bin/env python3
"""
Module for transforming a key and a numeric value into a key-value pair.

"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and a number (int or float).

    """
    return (k, float(v ** 2))
