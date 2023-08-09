#from replit import clear
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply,
  "/": divide
}

def calculator():
    
  print(logo)
  num1 = float(input("Enter the first number: "))
  for operator in operations:
    print(operator)
  should_continue = True
  
  while should_continue:
    operator_symbol = input("Pick an operator: ")
    num2 = float(input("Enter the second number: "))
    calculation = operations[operator_symbol]
    answer = calculation(num1, num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with this number {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      #clear()
      calculator()

calculator()
  
