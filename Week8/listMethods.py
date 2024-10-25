# Lists in Python - Recap

# Lists are collections of items.
# We use square brackets [] to define them.

# Example
#activities = ['soccer', 'reading', 'drawing', 'painting']
#print(activities)   # we print a list out using its name

# Each item in a list has an index number, starting from 0. 
# You can access individual items using their index.
#print(activities[0])  # This will print out the first activity, which is soccer

# You can change the value of an item in a list by 
# ___________ a new value to its index.
#activities[__________] = 'singing'  # This will change painting to singing.
#print(activities)

# You can retrieve a subset of a list using __________. 
# The syntax is list[x:y], where x is the ___________ index and 
# y is the __________ index (exclusive).
#first_three_activities = activities[__________:__________]  
#print(first_three_activities)

# You can combine two lists using the _____ operator.
#more_activities = ['cooking', 'hiking']
#all_activities = activities + more_activities  
#print(all_activities)

# You can remove an item from a list using the _______ statement or the .remove() method.
#del all_activities[__________]  # removes the last activity, 'hiking'
#print(all_activities)

# Lists can contain other lists, known as __________ lists. 
# This is useful for organizing related data.
#activity_durations = [['soccer', 60], ['reading', 30], ['painting', 45]] 
#print(activity_durations)

#print(activity_durations[__________][__________])  # access 'reading' duration.
#activity_durations[__________][__________] = 50  # Fill in the indices to update 'painting' duration.
#print(activity_durations)


# List Methods

# Initialize an empty list of animals
#animals = []

# len(): Get the size of the list
#size = _______
#print("The size of the list is:", size)

# .append(): Add items to the end of a list.
# Example: Add '__________' to the list.
#animals.append('__________')  # Fill in: Add your animal here

# .remove(): Remove a specific item by value.
# Example: Remove '__________' from the list.
#animals.append('__________')  # Fill in: Add an animal to remove later
#animals.remove('__________')  # Fill in: Replace with the animal to remove

# .pop(): Remove an item by index and return the removed item.
# Example: Remove the last animal and store it in a variable.
#last_animal = animals.pop()  # Removes the last animal

# .sort(): Sort the list alphabetically or numerically.
# Example: Sort the animals in alphabetical order.
#animals.append('__________')  # Fill in: Add an animal to sort
#animals.append('__________')  # Fill in: Add another animal to sort
#animals.sort()  # Sort the list

# Finding Items
# Use the 'in' keyword to check if an item exists in a list.
# Example: Check if '__________' is in the animals list.
#if '__________' in animals:  # Fill in: Replace with an animal to check
    # Fill in: Write what to do if the animal is found
#else:
    # Fill in: Write what to do if the animal is not found


# Use the .count() method to find how many times an item appears in the list.
# Example: Count how many times '__________' appears in the animals list.
#animal_count = animals.count('__________')  # Fill in: Replace with an animal
# Fill in: print out the count


# Use a for loop to iterate through a list.
# Example: Iterate and perform an action for each animal in the animals list.
#for animal in animals:
    # print out each animal

# The code above is a for loop!

# Exercise:
# - create a list of colors
# - add a few more colors using append, some can repeat
# - sort the list using the .sort() method
# - print the sorted list
# - remove the last element using pop
# - print out the updated list
# - count the number of times a certain colour appears in the list

colors = ['red', 'blue', 'yellow', 'green']
colors.append('black') 
colors.append('red')
colors.sort()
print(colors.sort)
last_color = colors.pop
print(colors)
colors_count = colors.count('red')
print(colors_count)