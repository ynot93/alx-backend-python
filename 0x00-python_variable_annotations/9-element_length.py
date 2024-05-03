#!/usr/bin/env python3
"""
Module to compute the length of elements in a given iterable of sequences.

"""

from typing import Iterable, List, Tuple, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of each element in a given iterable of sequences, returning a list of tuples.

    """
    return [(i, len(i)) for i in lst]
