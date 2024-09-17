# Strings - Strings can use double or single quotes.
# Print the word "Hello" using both double and single quotes.
#print("Hello")
print("Hello")
# Using quotes inside other quotes:
# You cannot use the same quotes inside, or it will cause an error.
# Example: Use a double-quoted string to include a single quote, or vice versa.
# Print: It's alright
# Print: He is called 'Johnny'
# Print: He is called "Johnny"
#print("It's alright Johnny")
#print("Johnny")
#print('"He is called Johnny"')
#print('"He is called Johnny"')
# Can set a string to a variable and then print it.
# Assign the word "Hello" to a variable and print it.
c = "a"
print(c)
# What is a String? 
# A string is an array of characters.
# A character is just one letter or symbol, in double quotes.
# The data type is still string
# Assign a single character to a variable and print it.
a = "Hello, World"
print(a[7])
# Accessing specific characters in a string:
# You can access different letters of a string using square brackets: stringName[index]
# Create a string and print out the element at index 7
print(a[0])
# In programming, we start counting at 0, so the first letter is at index 0.
# Print out the first element of the previous string
print(a[2:5])
# Slicing strings:
# You can return a range of characters by using slicing.
# Specify the start index and end index (not included), separated by a colon.
# Slice a string from position 2 to 5.
print(a[:5])
# Slice from the start:
# By leaving out the start index, the slice will start from the first character.
# Slice a string from the beginning up to index 5.
print(a[2:])
# Slice to the end:
# By leaving out the end index, the slice will include all characters starting from the given index to the end.
# Slice a string starting from index 2 to the end.
print(a[-5:-2])
# Negative indexing:
# You can use negative indexes to start counting from the end of the string.
# Get the characters from "o" in "World!" (position -5) to, but not including "d" in "World!" (position -2):
for c in "ottawa islamic school":
    print(c)
# Loop through the characters in a string:
# Use a for loop to iterate through each character in a string.
phrase = "Islam is to submit to Allah SWT dor all matter, personal adn societal"
print(len(phrase))
# Get the length of a string:
# Use the len() function to get the total number of characters in a string.
word = "I am muslim"
print("muslim" in word)
print("cat" in word)
print("u" in word)

# Checking if a certain phrase or character is in a string:
# You can check if a string contains a certain phrase or character using the keyword `in`.

# Concatenating strings:
# You can combine strings using the + operator.
a = "Watermelon"
b = "it's yummy"
print(a + " " + b )
# The upper() method returns the string in upper case:

# The lower() method returns the string in lower case:

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space. We can use strip()

# The replace() method replaces a string with another string