from random import randint

points: int = 0
#points: int
player: str = ""
NAMED_CONSTANT: str = "\U0001F920"
correct_number = (randint(1, 100))
def main():
  greet();
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
    
  # custom procedure
  # custom function
    # game loop

def greet() -> None:
    print("Hello, Welcome to guess a number! ")
    print("The goal of this game will be to guess a number between 1 and 100 in the fewest number of tries possible. The higher the point total the more wrong guesses you had! ")
    player = input(" Enter your name ")

def guess_number():
  guess = (input(" Guess a number between 1 and 100 "))
  guess = int(guess)
  number_of_tries = 0
  points = 0  
  while guess > 1 and guess < 100:
    if guess < correct_number:
      print("Higher, guess again ")
      points+=10
      number_of_tries+=1
    if guess > correct_number:
      print(" Lower, guess again ")
      points+=10
      number_of_tries+=1
    if guess == correct_number:
      print("Correct! ")
      break
    else: print(guess_number())

def total_points(points):
  water = input("How many glasses of water did you have today? ")
  additional_points = int(water) * int(10)
  total = (int(points) + int(additional_points))
  print(total)
print(f"{player} , you scored {points}")


if __name__ == "__main__":
    main()