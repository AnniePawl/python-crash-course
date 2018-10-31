# LOOPING through an Entire List
# Allows you to run throuh all entries in a list, performing the same task with each item
# Example- you have a list of magicians, you want to print each anme without called each individuallyself.
magicians = ['alice', 'betty','carl']
for magician in magicians:
    # print (magician)
# Line 2 tells python to pull a name from magicians and store it in a variable called, magician
# Print a message to each magician!
    print("Hi " + magician.title() + ", you did great!")
# Indentation! Everything indented after for/in statement in considered in the loop
# Code that is not indented will be executed once, without repetition
print ("Thank you, everyone! 'twas a gr8 show'")

# Another example:
dogs = ['spot','grizzly','slobbers']
for dog in dogs:
    print("My dog's name is, " + dog.title())

# Making Numerical Lists w/range function
# This will print 1 2 3 and 4 (one-off)
for value in range(1,5):
    print(value)

# You can use Range to Make a LIST OF NUMBERS
# wrap list() outside of range()
numbers = list(range(1,4))
print (numbers)
# List the even numbers between 1 and 10, then odd
even_numbers = list(range(2,11,2))
print(even_numbers)
odd_num = list(range(1,12,2))
print (odd_num)

# Simple Stats
# MIN and MAX functions
digits = [2,5,3,1,7,5,2,9,5,3,]
print (min(digits))
print(max(digits))
sum = sum(digits)
print (sum)

# Create a list of the first ten squared numbers
squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
print (squares)

# List Comprehensions
# Allow you to create a lot of functionality in one line of code. Combines "for loop" and creation of new elements
squares = [value**2 for value in range(1,11)]
print(squares)

# Working with Part of a List
# Slicing a LIST to work with subset
# Specify index of 1st and last elements(remember one-off)
# If you don't specify 1st of last index,
players = ['lila','lexi','laura','lauren','lydia']
print(players[0:2])

# Looping through a Slice
# You can use "for loop" on list subset
print ("Here are the players on my team: ")
for player in players[0:3]:
    print(player.title())

# Copying a List
# You can make a slice that includes entire original list by omitting first and second index([:]). This tells python to make a slice that starts at first item and ends at lastself.
annas_food = ['pizza','rice pudding', 'bagel']
kats_food = annas_food[:]
print (annas_food)
print (kats_food)

# TUPLES
# Allow you to create a list of items that cannot change. These items are called, Immutable
# Looks like a list, but uses () instead of []
# Ex- permenently define size of a rectangle
dimensions = (200, 30)
print (dimensions[0])
print (dimensions[1])
# If you try to replace a value, youll get an errror
# dimensions[0] = 250 won't work

#Looping through all values in a Tuple
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
# Can't modify a tuple, but can assign new value to variable that holds a tuple .
# To change rectangle dimensions, redefine entire Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
