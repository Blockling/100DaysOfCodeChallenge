#This Program is supposed to do the same things as the Coffemachine Program from 15Intermediate-CoffeeMachine, but it is programmed in OOP-style
#IMPORTANT: Everything but the main.py file is pre-done and NOT made by me
#ALSO IMPORTANT: Somehow I completed this assignement WITHOUT Documentation or any other help \(^_^)/
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
COFFEEMAKER = CoffeeMaker()
MONEYMACHINE = MoneyMachine()

is_on = True
order_phrase = "Order one of: " + str(MENU.get_items()) + "report"
while is_on:
    customer_request = input(order_phrase)
    if customer_request == "report":
        MONEYMACHINE.report()
    elif customer_request == "off":
        is_on = False
    else:
        if COFFEEMAKER.is_resource_sufficient(MENU.find_drink(customer_request)):
            cost = 0
            for Item in MENU.menu:
                if Item.name == customer_request:
                    cost = Item.cost
                    print(f"Bingo::{cost}")
            if MONEYMACHINE.make_payment(cost):
                COFFEEMAKER.make_coffee(MENU.find_drink(customer_request))
