"""Examples of using lists in a simple game"""

from random import randint


rolls: list[int] = list() # str(10) 
rolls.append(randint(1,6))
rolls.append(randint(1,6))


# Access an individual item
print(rolls[0])
print(rolls[1])
