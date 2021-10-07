"""List utility functions."""

__author__ = "730329515"


# TODO: Implement your functions here.
def all(li: list[int], n: int) -> bool:
    """All Function."""
    if len(li) == 0:
        return False
    i: int = 0
    length: int = len(li)
    while i < length:
        if li[i] != n:
            return False
        i += 1
    return True


def is_equal(li1: list[int], li2: list[int]) -> bool:
    """Is Equal Function."""
    i: int = 0 
    length: int = len(li1)
    if length != len(li2):
        return False
    
    while i < length:
        if li1[i] != li2[i]:
            return False
        i += 1
        
    return True


def max(li: list[int]) -> int:
    """Max Function."""
    if len(li) == 0:
        raise ValueError("max() arg is an empty List")
    m: int = li[0]
    i: int = 0
    length = len(li)
    while i < length:
        if m < li[i]:
            m = li[i]

        i += 1

    return m