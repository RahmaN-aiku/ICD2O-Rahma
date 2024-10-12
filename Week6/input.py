#In class assignment October 10 2024
# input is used to get data from a person

name = input("What is your name? ")     # aprompt must be given in the brackets

# when i run program waits for user to respond
# when user puts enter, program continues
print("Rahma")
print(" Hi " + "Rahma" )

age = input("What is your age? ")
print("You are: " + age + " Years old")

# Exercise 1:
age = input("How old are you? ")
print(" You are 14 ")
ten_years = input("How old are you going to be in ten years? ")
print("24 years old")

# Exercise 2:
name = input("What is your name? ")
print("Riyaq")
print(len(name))
print(name[::-1])

# Exercise 3:
num1 = 10
num2 = 14
print(num1 + num2)
print(num1 * num2)

# Exercise 4:
height_meters = 1.64
centimeters = height_meters*100
print("Your height in centimeters is", height_meters*100)

# Exercise 5:
age = 14
if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - age
    print("You are not eligible to vote you have", years_left)

# Exercise 6:
num = -7
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Exercise 7:
num1 = 9
num2 = 13
num3 = 16
largest = num3
if num1 > largest:
    print("largest = num1")
elif num2 > largest:
    print("largest = num2")
else: 
    print("largest = num3")

# Exercise 8:
preference = "pizza"
if preference == "burgers":
    print("Pizza was invented in Italy!")
elif preference == "burgers":
    print("Burgers are most popular in the USA!")
elif preference == "pasta":
    print("There are over 600 types of pasta!")
else:
    print("You did not pick one of the options!")