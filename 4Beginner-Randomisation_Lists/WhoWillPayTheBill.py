#Program that takes a list of names as input and then decides who will pay the bill by random
#seperate list: take str input -> use list = str.split(", ") to split the str into a list 

import random as r

print("Input all the Names, seperating them with a comma and a space: , ")
user_names = input()

string_names = user_names.split(", ")

randomNumber = r.randint(0, len(string_names))
print(string_names[randomNumber])