#Program that will flip a coin and output the result(head, tails)
#https://www.geeksforgeeks.org/python-randint-function/

import random as r

coin = r.randint(0,1)
#print(coin)

if coin == 0:
    print("Tails")
if coin == 1:
    print("Heads")