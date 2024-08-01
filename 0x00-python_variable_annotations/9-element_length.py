#!/usr/bin/env python3
"""
A function annotated to take an iterable as a paramter
and return a list containing a tuple
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns A list containing a tuple
    """
    return [(i, len(i)) for i in lst]
