import datetime

#Get current year
now = datetime.datetime.now()

name = input("Give me your name: ")
age = input("Enter your age: ")
# Calculate year to turn 100
year100 =  now.year + (100-int(age))
# Print result
print("Your name is " + name)
print("You will turn 100 years old in " + str(year100))
