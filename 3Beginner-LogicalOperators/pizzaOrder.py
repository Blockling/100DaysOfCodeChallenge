#This program will ask the user what pizza they want and then calculate the prize of the pizza

print("Welcome to Python Pizza Deliveries")
user_size = input("What size Pizza do you want? S/M/L ")
user_pepperoni = input("Do you want extra Pepperoni? Y/N ")
user_cheese = input("Do you want extra cheese? Y/N ")
totalPrice = 0

if user_size == "S":
    totalPrice += 15
if user_size == "M":
    totalPrice += 20
if user_size == "L":
    totalPrice += 25
if user_pepperoni == "Y" and user_size == "S":
    totalPrice += 2
if user_pepperoni == "Y" and (user_size == "M" or user_size == "L"):
    totalPrice += 3
if user_cheese == "Y":
    totalPrice += 1
    
print("Thank you for your Order! Your total is:", totalPrice)