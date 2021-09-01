"""Relational Operators."""

__author__ = "730329515"

left: str = (input("Left-hand side: "))
right: str = (input("Right-hand side: "))
print(left + " < " + right + " is " + str(int(left) < int(right)))
print(left + " >=" + right + " is " + str(int(left) >= int(right)))
print(left + " == " + right + " is " + str(int(left) == int(right)))
print(left + " != " + right + " is " + str(int(left) != int(right)))