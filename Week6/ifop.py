# if statements allow for branches in the code
# nested if statements allow us to check multiple conditions in one branch of our code

# example - question 1 from nestedif.py
# simulating a traffic light: pay attention to the conditions and the order!
lightColour = "red"
if  (lightColour!= "red"):
    if (lightcolour == "green"):
            print("Go")
    else:
        print("Caution, prepare to stop")
else:
    print("Stop")
# __________________ also allow us to check multiple conditions in one branch
# three logical operators: ________ __________ _________

# example - nested if statements
raining = True
ownUmbrella = False

if raining:
    if ownUmbrella:
        print("I will be dry.")
    else:
        print("I should have bought an umbrella.")
else: 
    print("Today is a sunny day!")

# same example with logical operators
#if raining and ownUmbrella:
#    print("I will be dry.")
#elif raining and not ownUmbrella:   # True and not False = True and True = True
#    print("I should have bought an umbrella.")
#else:
#    print("Today is a sunny day!")

# We will negate the value - not True = False, not False = true
# guided example
age = 20
is_citizen = True

if (age >= 18 and is_citizen):  # what goes here instead of the parentheses?
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# nested if statements are good when checking multiple conditions one after the other (depending conditions)
# logical operators allow us to check for multiple conditions is a single expression (at once)
# logical operators can be a little harder to code, but are more concise
# unless I specifically say to use one or the other, you can use whichever

# exercises
# 1. Write a program that checks if a student is eligible for a scholarship.
#   A student is eligible if they have a GPA of 3.5 or higher and they participate in extracurricular activities.


# 2. Write a program that simulates a simple login system.
# Check if the username is "admin" and the password is "1234". If both are correct, print "Access granted.". If the username is wrong, print "Incorrect username.". If the password is wrong, print "Incorrect password.".