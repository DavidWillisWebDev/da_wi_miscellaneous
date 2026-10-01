import random

# Casino project

# this casino will keep track of your wallet

# Roulette

# First, you choose a number or color.
# Then, you bet the money to put into the game.
# Next, you spin the wheel.
# After you spin the wheel, the ball lands on a number. Your points vary on the outcome. If you guess a color successfully, then you get double your points. If you guess a number successfully, then you get five times your points.

money = 100
print("you have " + str(money) + " dollars")

def roulette():
  global money
  colors = ["black", "red"]
  
  # Note: Number variable goes clockwise.
  numbers = []
  for i in range(36):
    numbers.append(i)

  actualNumber = random.choice(numbers)
  if actualNumber % 2 == 0:
    color = "black"
  else:
    color = "red"
  validChoice = False
  while not validChoice:
    playerChoice = input("Choose a number from 0-35 or choose between Black or Red:\n")
    if playerChoice.isdigit():
      playerChoice = int(playerChoice)
      if playerChoice not in numbers:
        print("That is not a valid answer. Try again.")
    elif playerChoice not in colors:
      print("That is not a valid answer. Try again.")
    else:
      validChoice = True
      

  validChoice = False
  while not validChoice:
    bet = input("How much do you bet?\n")
    if bet.isdigit() == False:
      print("That is not a valid answer. Try again.")
    else:
      bet = int(bet)
      if bet > money:
        print("You do not have the money for that. Try again.")
      elif bet < 1:
        print("You cannot bet negative numbers. Try again.")
      elif bet == 0:
        print("You need something to bet, or you cannot play. Try again.")
      else:
        money -= bet
        validChoice = True
  print("The wheel has landed on " + str(actualNumber) + ", " + color)
  if isinstance(playerChoice, int):
    if playerChoice == actualNumber:
      money += bet * 5
      print("You win.")
    else: 
      print("You lost.")
  else:
    if playerChoice == color:
      money += bet * 2
      print("You win.")
    else:
      print("You lose.")
  print("you now have " + str(money) + " dollars")

roulette()