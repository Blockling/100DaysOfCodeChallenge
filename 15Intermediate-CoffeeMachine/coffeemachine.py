#This program simulates a virtual coffee machine
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
profit = 0

def checkRessourcesSufficient(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there isnt enough {ingredient} to make this drink")
            return False
    return True

def countCoins(price):
    print("Insert your coins now:")
    TwoEuroCoins = int(input("Insert 2 Euro Coins")) * 2
    OneEuroCoins = int(input("Insert 1 Euro Coins"))
    FiftyCentCoins = int(input("Insert 50 Cent Coins")) * 0.5
    TwentyCentCoins = int(input("Insert 20 Cent Coins")) * 0.2
    TenCentCoins = int(input("Insert 10 Cent Coins")) * 0.1
    total = TwoEuroCoins + OneEuroCoins + FiftyCentCoins + TwentyCentCoins + TenCentCoins
    if total < price:
        print("You have not inserted enough coins")
        return False
    if total > price:
        print("Your Change is ", round(total - price, 3))
        return True

def makeDrink(order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]       
    return True

is_on = True
while is_on:
    user_prompt = str(input("What would you like? (espresso/latte/cappuccino):"))
    if user_prompt == "off":
        is_on = False
    elif user_prompt == "report":
        print(f"Profit€ {profit}")
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
    else:
        drink = MENU[user_prompt]
        if checkRessourcesSufficient(drink["ingredients"]):
            if countCoins(drink["cost"]):
                profit+=drink["cost"]
                makeDrink(drink["ingredients"])
                print(f"Your {user_prompt} has been made. Enjoy!")