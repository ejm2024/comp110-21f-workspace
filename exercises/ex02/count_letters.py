"""Counting letters in a string."""

__author__ = "730329515"


# Begin your solution here...
lt: str = input("What letter do you want to search for? ")
wd: str = input("Enter a word ")
counter: int = 0
index: int = 0
letter: str = " "
while index < len(wd):
    letter = wd[index]
    index = index + 1
    if lt == letter:
        counter = counter + 1
print("count: " + str(counter))