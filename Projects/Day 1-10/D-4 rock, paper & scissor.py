import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
signs = [rock, paper, scissors]
#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor.\n"))
if user_choice >= 0 and user_choice < 3:
  print(signs[user_choice])
  

  computer_choice = random.randint(0,2)
  print("Computer choice:")
  print(signs[computer_choice])

  if user_choice == computer_choice:
    print("It's a draw.")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif user_choice < computer_choice:
    print("You lose")
  

else:
  print("Invalid number, You lose")
