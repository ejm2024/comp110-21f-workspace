"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730329515"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
cookie: int = int(randint(1, 4))

print("Your fortune cookie says... ")
if cookie == 1:
    print(" You will have a great day. ")

if cookie == 2:
    print(" You will recieve a check. ")

if cookie == 3:
    print(" Order pizza tomorrow. ")

if cookie == 4:
    print(" You will have a good weekend. ")

print(" Now, go spread positive vibes! ")