# Importing Python libraries
import random
# End Imports

# Global Variables
# Computer generating a random number between 0 and 10
ComputerNumber = random.randint(0,10)

# Defining the largest number of allowable guesses
GuessMax = 3

Win = False
Play = True

print("Welcome to the Number Guessing Game!\n\n")
print("You have " + str(GuessMax) + " guesses for each round")
# Looping on game play
while Play == True:
  while GuessMax > 0:
    PlayerGuess = input("Enter a number between 0 and 10: ")
    PlayerGuess = float(PlayerGuess)

    if (PlayerGuess < 0 or PlayerGuess >10):
      print("Bad input! Only number between 0 and 10 inclusively")
      break
    else:
      if (PlayerGuess > ComputerNumber):
        print("Your guess was too big!")
      elif (PlayerGuess < ComputerNumber):
        print("Your guess was too small!")
      else:
        print("You guessed correctly!!!")
        Win = True
        break
      GuessMax = GuessMax-1
      print("You have " + str(GuessMax) + " guess left")

  if Win == True:
    print("Congratulations! You won at " + str(GuessMax) + " tries")
  else:
    print("No more guesses left!")
    print("The number was: " + str(ComputerNumber))

  answer = input("Would you like to play again? Y/N ")
  if answer == "N" or answer == "n":
      print("OK. Goodbye!")
      Play = False
  else:
    Win = False
    GuessMax = 3
      
