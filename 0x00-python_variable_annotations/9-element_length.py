#!/usr/bin/env python3
"""
Module to compute the length of elements in a iterable.

"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute length of element in a iterable of sequences.

    """
    return [(i, len(i)) for i in lst]
