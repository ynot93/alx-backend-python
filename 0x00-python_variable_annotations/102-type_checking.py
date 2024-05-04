#!/usr/bin/env python3
"""
Module for functions for manipulating sequences of integers.

"""

from typing import List, Tuple, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Multiplies each item in a tuple by a certain factor.

    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), 3)
