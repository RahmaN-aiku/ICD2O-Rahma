# For Loops in Python

# A for loop is used to iterate over a ____________ (like a list).
# It allows you to execute a block of code ____________ for each item in the sequence.

# Example: Here is our list
animals = ['ant', 'cat', 'dog', 'aardvark', 'rabbit', 'elephant', 'anteater']

# Structure to iterate through each item in the sequence.
#     for item in sequence:
#       code that should run for each item
 
# Example: print out each animal
for animal in animals:
    __________ 

# You can also use the range() function to loop through a ___________ of numbers.
# Example: Loop from 0 to 4, print out each number divided by 2
for i in range(5):  # This will generate numbers from 0 to 4
    __________  

# Read more about range here (scroll down): https://www.w3schools.com/python/python_for_loops.asp 

# Example: Use a for loop to create a new list of animal names in uppercase
uppercase_animals = []  # Initialize an empty list

for animal in animals:
    # Convert each animal name to uppercase and add it to the new list
    uppercased = ___________
    uppercase_animals.append(______)  # Fill in: Add the uppercase animal

# At this point, uppercase_animals contains all animal names in uppercase.
# Print out the the uppercase list

# Use a for loop to count the number of animals in the original list, that start with a
a_count = 0  # Initialize a counter

for animal in animals:
    if __________:
        a_count += 1  # Increase the count for each animal

# print out count of animals that start with a
print("The number of animals that start with the letter a is:", a_count)

# For loops also work with strings
for letter in "elephant":
    ______________

# break statement allows us to exit a for loop before it completes
fruits = ['apple', 'banana', 'plum', 'berry']
for fruit in fruits:
    if _________________:
        break


# Summary
# - For loops allow you to iterate over a sequence.
# - You can use them with lists, strings, and more.
# - The range() function generates a sequence of numbers for looping.

# EXERCISE 1: Create a for loop to add the lengths of each name in names, 
# to a list called name_lengths
names = ['Alice', 'Bob', 'Charlie', 'David']
name_lengths = []

# EXERCISE 2: Write a for loop that calculates the sum of the numbers in nums
nums = [2, 5, 6, 1, 4, 3]

# EXERCISE 3: Print out all the even numbers between 1 and 20 inclusive


# EXERCISE 4: Ask the user for a phrase. Use a for loop to count how many
# times the letter A shows up.


# EXERCISE 5: Ask the user for a number 10 times. For each number, add its
# square to a list called squares
squares = []