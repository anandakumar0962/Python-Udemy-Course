# To clear the console for each execution for new comparison use clear() function in replit.
from art import logo, vs
from game_data import data
import random

def compare(celebrity_A, celebrity_B, user_guess):
    """Validate the user guess."""
    if (celebrity_A['follower_count'] > celebrity_B['follower_count'] and user_guess == 'A') or (celebrity_A['follower_count'] <  celebrity_B['follower_count'] and user_guess == 'B'):
        return True
    return False

def print_details(celebrity_A, celebrity_B):
    """ Print the celebrity details in the console."""
    print(f"Compare A: {celebrity_A['name']}, a {celebrity_A['description']}, from {celebrity_A['country']}.")
    print(vs)
    print(f"Against B: {celebrity_B['name']}, a {celebrity_B['description']}, from {celebrity_B['country']}.")

def get_details(celebrity_A, celebrity_B):
    if celebrity_A == None and celebrity_B == None:
        celebrity_A = random.choice(data)
        celebrity_B = random.choice(data)
        while celebrity_A == celebrity_B:
            celebrity_B = random.choice(data)
    else:
        celebrity_A = celebrity_B
        celebrity_B = random.choice(data)
    return celebrity_A, celebrity_B

def game():
    print(logo)
    celebrity_A = None
    celebrity_B = None
    game_over = False
    score = 0
    while  not game_over:
        celebrity_A, celebrity_B = get_details(celebrity_A, celebrity_B)
        print_details(celebrity_A, celebrity_B)
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        result = compare(celebrity_A, celebrity_B, user_guess)
        if result:
            score += 1
            print(f"You are right! Your current score is {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

game()