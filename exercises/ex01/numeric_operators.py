"""Numeric Operators."""

__author__ = "730329515"

left: str = (input("Left-hand side: "))
right: str = (input("Right-hand side: "))
x = int(left)
y = int(right)
print(left + " ** " + (right) + " is " + str(x **y ))
print(left + " / " + (right) + " is " + str(x / y ))
print(left + " % " + (right) + " is " + str(x % y))
print(left + " // " + (right) + " is " + str(x // y))