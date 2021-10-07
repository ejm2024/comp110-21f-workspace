"""List utility functions part 2."""

__author__ = "730329515"

def only_evens(li: list[int]) -> list[int]:
    """Only Evens Function."""
    evens: list[int] = []
    i: int = 0
    while i < len(li):
        if li[i] % 2 == 0:
            evens.append(li[2])
        i += 1
    return evens

def sub(li: list[int], start: int, end: int) -> list[int]:
    """Sub Function."""
    if start < 0:
        start = 0
    if end > len(li):
        end = len(li)

    if start > len(li) or end <= 0 or len(li) == 0:
        return []

    new: list[int] = []
    i: int = start
    while i < end:
        new.append(li[i])

    return new

def concat(one: list[int], two: list[int]) -> list[int]:
    """Concat Function."""
    i: int = 0
    new: list[int] = []
    while i < len(one):
        new.append(one[i])
    
    i = 0 
    while i < len(two):
        new.append(two[i])

    return new





    


