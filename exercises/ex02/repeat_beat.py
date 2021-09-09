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
    while tms > 0:
        print(str(bt))
        tms = tms - 1