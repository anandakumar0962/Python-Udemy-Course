#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5
def set_difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard'.").lower()
  if choice == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL

def check_answer(guess, answer, life):
  if guess > answer:
    print("Too High")
    return life-1
  elif guess < answer:
    print("Too Low")
    return life-1
  else:
    print(f"You got it! The answer was {answer}.")
def game():
  print(logo)
  print("Welcome to number guessing game")
  print("I'm thinking of number from 1 to 100")
  answer = random.randint(1,100)
  life = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {life} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    life = check_answer(guess, answer, life)
    if life == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again")

game()

