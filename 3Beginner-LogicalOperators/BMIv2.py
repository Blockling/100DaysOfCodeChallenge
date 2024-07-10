#BMI calculator that claculates you BMI and the also tells you if ur underweight, overweight etc

#copy BMI calculator from 2Beginner - DataTypes

user_weight = input("What is your Weight? ex:60 ")
user_height = input("What is your height? ex:1.6 ")

BMI = int(user_weight)/(float(user_height)*float(user_height))
print(int(BMI))

#use if statements to determine if youre overweight etc:
#Under 18.5 underweight - to 25 normal weight - to 30 overweight - to 35 obese - above 35 clinically obese

if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are normal weight")
elif BMI < 30:
    print("Your are overweight")
elif BMI < 35:
    print("You are obese")
else:
    print("You are clinically obese")
    
