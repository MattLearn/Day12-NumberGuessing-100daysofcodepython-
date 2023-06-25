#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random


def generate_number():
  return random.randint(1, 100)

def win_test(guess, answer):
  if guess > answer:
    print("Too High")
    return False
  elif guess < answer:
    print("Too Low")
    return False
  else:
    print("Correct")
    return True

def play_cycle(chances):
  clear = False
  print("I'm thinking of a number between 1 and 100")
  answer = generate_number()
  for number in range(chances,0,-1):
    print(f"you have {number} guesses left")
    guess = int(input("What number am I thinking of? "))
    clear = win_test(guess, answer)
    if clear == True:
      print("You got it!")
      break
  print(f"The number I was thinking of is {answer}")
  if (clear ==False):
    print("Better luck next time!")
  
def game_difficulty():
  mode = input("Easy(e) or Hard(h): ").lower()
  if mode == 'e':
   play_cycle(10)
  elif mode =='h':
    play_cycle(5)
  else:
    print("Please enter 'e' or 'h'")
    game_difficulty()

print("Welcome to Guess the number!")
print("Would you like to play?")
while True:
  choice = input("Yes(y) or No(n)").lower()
  if choice == 'y':
    game_difficulty()
    print("Play again?")
  elif choice == 'n':
    print("Take Care")
    break
  else:
    print("Please enter 'y' or 'n'")