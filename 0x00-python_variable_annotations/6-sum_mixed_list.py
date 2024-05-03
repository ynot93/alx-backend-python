#!/usr/bin/env python3
"""
Module for summing a list of integers and floating-point numbers.

"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list containing both integers and floating-point numbers,
    returning the sum as a float.

    """
    return float(sum(mxd_lst))
