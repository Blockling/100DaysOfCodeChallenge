#Program that tells you how many days, weeks or months you have left in your life, assuming you will live until 90 years old (not substracting days from weeks etc.)

#1 year = 365 days; 1 year = 52 weeks; 1 year = 12 months
user_age = int(input("What is your current age? "))

years_left  = 90 - user_age
days_left   = 365 * years_left
weeks_left  = 52 * years_left
months_left = 12 * years_left

print(f"You have: {days_left} days, {weeks_left} weeks or {months_left} months left in your life")