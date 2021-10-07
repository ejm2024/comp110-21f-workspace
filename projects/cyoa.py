"""Import Random Int."""
from random import randint

"""Guess a random number. """

__author__: str = "730329515"

points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U0001F920"
correct_number = (randint(1, 100))


def main() -> None:
    """Main Function."""
    greet()
    playing = True
    version: str
    while playing:
      version = input("Do you want to play the regular version, bonus version, or stop? Respond with: regular, bonus, or stop." + " " + NAMED_CONSTANT)
      if (version == "regular"):
        guess_number()
      if (version == "bonus"):
        total_points(points)
      if (version == "stop"):
        playing = False


def greet() -> None:
    """Welcome Greeting Function."""
    print("Hello, Welcome to guess a number! ")
    print("The goal of this game will be to guess a number between 1 and 100 in the fewest number of tries possible. The higher the point total the more wrong guesses you had! ")


def guess_number() -> None:
    """Regular Game Function."""
    guess = (input(" Guess a number between 1 and 100 "))
    guess2 = int(guess)
    number_of_tries = 0
    points = 0
    while guess2 > int(1) and guess2 < int(100):
      if guess2 < correct_number:
        print("Higher, guess again ")
        points += int(10)
        number_of_tries += int(1)
        if guess2 > correct_number:
          print(" Lower, guess again ")
        points += int(10)
        number_of_tries += int(1)
        if guess2 == correct_number:
          print("Correct! ")
          break


def total_points(points) -> None:
    """Bonus Game Function."""
    water = input(str("How many glasses of water did you have today? "))
    additional_points = int(water) * int(10)
    total = (int(points) + int(additional_points))
    print(total)


print(f"{player} , you scored {points}")


if __name__ == "__main__":
    main()