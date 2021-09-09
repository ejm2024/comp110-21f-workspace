"""Repeating a beat in a loop."""

__author__ = "730329515"


# Begin your solution here...
from random import randint
from typing import Counter

bt: str = input("What beat do you want to repeat? ")

tms = int(input("How many times do you want to repeat it? "))

if tms <= 0:
    print("No beat...")

else: 
    ck: str = bt
    while tms > 1:
        ck = ck + " " + bt
        tms = tms - 1
    print(ck)