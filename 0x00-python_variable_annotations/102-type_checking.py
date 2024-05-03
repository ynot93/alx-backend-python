#!/usr/bin/env python3
"""
Module for providing utility functions for manipulating sequences (lists and tuples)
of integers.

"""

from typing import List, Tuple, Union

def zoom_array(lst: Union[Tuple[int, ...], List[int]], factor: int = 2) -> List[int]:
    """
    Multiplies each item in a tuple or list by a certain factor and returns a list.

    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
