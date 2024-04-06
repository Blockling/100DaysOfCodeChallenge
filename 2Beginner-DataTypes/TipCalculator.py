#This program will calculate how much multiple people will have to pay including tip and diving it by how many people split the bill. It will also round those numbers

#ask the user to provide information on the bill
user_bill = float(input("How much is the bill? "))
user_tip = int(input("How much do you want to tip (as int: 10,12,15)? "))
user_people = int(input("How many people are splitting the bill? "))

#convert the tip to percentages and multiply the bill to match
tip_percentage = user_tip/100 + 1

bill_total = user_bill*tip_percentage
bill_perPerson = round((bill_total / user_people), 2)

print(f"Your total bill is: {round(bill_total)}, which means every person should pay: {bill_perPerson}")