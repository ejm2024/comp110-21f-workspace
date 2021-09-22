"""Finding duplicate letters in a word."""

__author__ = "730329515"


x = input(("Enter a word:"))
i: int = 0
brk: bool = False
while (i < len(x) - 1):
    if (brk == True):
        break
    j: int = i + 1
    while (j < len(x)):
        if (x[i] == x[j]):
            print("Found duplicate: True")
            brk = True
            break
        else:
            j += 1
    i += 1
if (brk == False): 
    print("Found duplicate: False")