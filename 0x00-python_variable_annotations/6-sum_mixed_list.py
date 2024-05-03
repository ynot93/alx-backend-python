#!/usr/bin/env python3
"""
Module for summing a list of integers and floating-point numbers.

"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute sum of list of integers and floats.

    """
    return float(sum(mxd_lst))
