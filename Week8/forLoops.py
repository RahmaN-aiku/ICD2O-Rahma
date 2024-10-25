# For Loops in Python (COMPLETED)

# A for loop is used to iterate over a sequence (like a list).
# It allows you to execute a block of code repeatedly for each item in the sequence.

# Example: Here is our list
animals = ['ant', 'cat', 'dog', 'aardvark', 'rabbit', 'elephant', 'anteater']

# Structure to iterate through each item in the sequence.
#     for item in sequence:
#       code that should run for each item
 
# Example: print out each animal
for animal in animals:
    print(animal) 

# You can also use the range() function to loop through a sequence of numbers.
# Example: Loop from 0 to 4, print out each number divided by 2
for i in range(5):  # This will generate numbers from 0 to 4
    print(i/2)  

# Read more about range here (scroll down): https://www.w3schools.com/python/python_for_loops.asp 

# Example: Use a for loop to create a new list of animal names in uppercase
uppercase_animals = []  # Initialize an empty list

for animal in animals:
    # Convert each animal name to uppercase and add it to the new list
    uppercased = animal.upper()
    uppercase_animals.append(uppercased)  # Fill in: Add the uppercase animal

# At this point, uppercase_animals contains all animal names in uppercase.
# Print out the the uppercase list
print(uppercase_animals)

# Use a for loop to count the number of animals in the original list, that start with a
a_count = 0  # Initialize a counter

for animal in animals:
    if animal.startswith('a'):
        a_count += 1  # Increase the count for each animal

# print out count of animals that start with a
print("The number of animals that start with the letter a is:", a_count)

# For loops also work with strings
for letter in "elephant":
    print(letter)


# Summary
# - For loops allow you to iterate over a sequence.
# - You can use them with lists, strings, and more.
# - The range() function generates a sequence of numbers for looping.

# EXERCISE 1: Create a for loop to add the lengths of each name in names, 
# to a list called name_lengths
names = ['Alice', 'Bob', 'Charlie', 'David']
name_lengths = []
for name in names:
    name_lengths.append(len(name))
    print(name_lengths)

# EXERCISE 2: Write a for loop that calculates the sum of the numbers in nums
nums = [2, 5, 6, 1, 4, 3]
total_sum = 0
for num in nums:
    total_sum += num
    print(total_sum)
# EXERCISE 3: Print out all the even numbers between 1 and 20 inclusive
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# EXERCISE 4: Ask the user for a phrase. Use a for loop to count how many
# times the letter A shows up.
phrase = ("Computers is really fun")
count_a = 0
for char in phrase:
    if char.upper() == 'A':
        count_a += 1
print("The letter 'A' appears", count_a, "times.")

# EXERCISE 5: Ask the user for a number 10 times. For each number, add its
# square to a list called squares
squares = []
for _ in range(10):
    number = int(input("10:"))
    squares.append(number ** 2)
    print(squares)
