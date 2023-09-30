MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

def make_coffee(coffee_type):
    if coffee_type == 'espresso':
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    elif coffee_type == 'latte':
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    else:
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    print(f"Here is your {coffee_type}. Enjoy!")

def payment(cost):
    global money
    print("Please insert coins.")
    no_of_quarters = int(input("how many quarters?: "))
    no_of_dimes = int(input("how many dimes?: "))
    no_of_nickles = int(input("how many nickles?: "))
    no_of_pennies = int(input("how many pennies?: "))
    change = round(((0.25*no_of_quarters)+(0.10*no_of_dimes)+(0.05*no_of_nickles)+(0.01*no_of_pennies)-cost), 2)
    money += cost
    if change<0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${change} in change.")

def check_resources(coffee_type):
    ingredients_needed = MENU[coffee_type]["ingredients"]
    if coffee_type == "espresso":
        if resources["water"] > ingredients_needed["water"] and resources["coffee"] > ingredients_needed["coffee"]:
            payment(MENU[coffee_type]["cost"])
            make_coffee(coffee_type)
        else:
            print("Sorry there is no enough resource.")
    elif coffee_type == "latte" or coffee_type == "cappuccino":
        if resources["water"] > ingredients_needed["water"] and resources["coffee"] > ingredients_needed["coffee"] and resources["milk"] > ingredients_needed["milk"]:
            payment(MENU[coffee_type]["cost"])
            make_coffee(coffee_type)
        else:
            print("Sorry there is no enough resource.")

let_continue = True
types_of_coffee = ["espresso", "latte", "cappuccino"]
while let_continue:     
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice in types_of_coffee:
        check_resources(user_choice)
    elif user_choice == 'report':
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f"Money: {money}")
    else:
        let_continue = False