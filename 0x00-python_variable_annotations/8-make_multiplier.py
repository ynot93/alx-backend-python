#!/usr/bin/env python3
"""
Creates a function that multiplies a number by a multiplier.

"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies its input by a multiplier.

    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
