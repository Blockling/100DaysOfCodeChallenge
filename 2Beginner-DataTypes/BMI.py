#Program that calculates the BMI using the formula: weight/height^2

user_weight = input("What is your Weight? ex:60")
user_height = input("What is your height? ex:1.6")

BMI = int(user_weight)/(float(user_height)*float(user_height))
print(int(BMI))