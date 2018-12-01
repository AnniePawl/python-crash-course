# PRINT STATEMENT
'''The easiest way to get python program to communicate with you via the terminal.
*Dont Forget, in Python3, print statement needs parenthesis()
'''
print ("Hello World")

# MY FIRST VARIABLE
message = "Life is Good"
print (message)
'''Variable Rules:
 - Can contain letters, numbers, underscore
 - Cannot start with a number
 - NO spaces, use underscore
 - Names should be short and descriptive
 '''

# STRING METHODS
name = "Ada Lovelace"
print (name.title())
print (name.upper())
print (name.lower())
''' .title() method that transforms name to title case.
.upper() will make all uppercase of data. Always  .lower() will make all lowercase
'''

# CONCATENATING STRINGS
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())
print("Hello, " + full_name.title())

# ESCAPING STRINGS
'''(\n) adds a new line
(\t) adds a new tab
(.rstrip) strips right whitespace
(.lstrip) strips left whitespace
'''
print("\tPython")
print ("Hey there" "\nHandsome")

# WORKING WITH NUMBERS
'''Integers  (Whole Numbers)
   Arithmetic Operators
   Addition (+)
   Subtraction (-)
   Multiplication (*)
   Division (/)
   Python supports oder of operations! Careful
'''
print (2 + 3)
print (5 * 4)

# AVOIDING TYPE ERRORS w/ STRINGS
'''Be careful when working w/ various types.
   Make sure to tell python how to interpret certain values
'''
age = 25
name = "Linda"
message = "Happy " + str(age) + " birthday, " + name
print(message)
