#!/usr/bin/env python3
"""
Module for safely retrieving the first element from a sequence.

"""

from typing import Any, Sequence, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Return the first element of a sequence or None if the sequence is empty.

    """
    if lst:
        return lst[0]
    else:
        return None
