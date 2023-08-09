from replit import clear
from art import logo
print(logo)

bidders = {}
should_continue = True
print("Welcome to the secret aution program.")

def highest_bidder(bidders):
  highest_amount = 0
  winner = ''
  for bidder in bidders:
    if bidders[bidder] > highest_amount:
      highest_amount = bidders[bidder]
      winner = bidder
  clear()
  print(f"The winner is {winner} with a bid of ${highest_amount}.")    

while should_continue:
  name = input("What's your name? ")
  bid = int(input("What's your bid? $"))
  bidders[name] = bid
  any_bidders = input("Any other bidders? Type 'yes' or 'no'.\n").lower()
  if any_bidders == 'yes':
    clear()
  else:
    should_continue = False
    highest_bidder(bidders)
  
