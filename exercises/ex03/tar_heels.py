"""An exercise in remainders and boolean logic."""

__author__ = "730329515"
# Begin your solution here...
a= int(input(" Enter an int "))
if (a % 2) == 0 and (a % 7) == 0:
    print("TAR HEELS")
elif (a % 7) == 0:
    print("HEELS")
elif (a % 2) == 0:
    print("TAR")
else:
    print("CAROLINA")