#!/usr/bin/env python3
"""
Module for creating a function that multiplies a number by a specified multiplier.

"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies its input by a specified multiplier.

    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
