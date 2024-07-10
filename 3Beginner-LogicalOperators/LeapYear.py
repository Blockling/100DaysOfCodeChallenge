#Program that figures out if given year is a leap year (February has a 29th day)
#Rules are:
#A leap year is a year where:
#on every year that is evenly divisible by 4		TRUE -> LEAP
#EXCEPT every year that is evenly divisible by 100	TRUE -> NOT LEAP
#UNLESS the year is also evenly divisible by 400	
#case1 HAS to be true; if case1 is true, but case2 is true, then false;     but if case 1 is true, case2 is false, but case3 is true, then true

#comment after code was done: this was a real mindfuck

user_year = int(input("Year to check: "))

case1 = user_year % 4
case2 = user_year % 100
case3 = user_year % 400

answer_true = "This year is a leap year"
answer_false = "This year is NOT a leap year"

if (case1)==0:  #this HAS to be true
    print("case1 True")
    
    if (case2)==0: #this will "false the true"
        print("case2 true")
        if (case3)==0:
            print("case3 true")
            print(answer_true)
        else:
            print("case3 false")
            print(answer_false)
    else:
        print("case2 false")
        print(answer_true)
 
else:
    print("case1 false")
    print(answer_false)


