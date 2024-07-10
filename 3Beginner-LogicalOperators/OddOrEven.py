#This Program checks if a number is odd or even

user_input = int(input("Input the number you want to check: "))
remainder = user_input % 2 #checkng if there is a remainder when you divide by 2
#if remaider = 0, number is even; if remainder != 0, number is odd
if remainder == 0:
    print("Your number is even")
else:
    print("Your number is odd")
