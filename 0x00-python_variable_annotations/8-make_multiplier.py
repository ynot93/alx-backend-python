#!/usr/bin/env python3
"""
Module for creating a function that multiplies a number by a specified multiplier.

"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies its input by a multiplier.

    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
