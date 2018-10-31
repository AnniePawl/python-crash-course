# Print Statement-- easiest way to get python program to communicate with you via terminalself.
#Dont' forget! In Python3, print statement needs parenthesis
print ("Hello World")

#My First Varable!
message = "Life is Good"
print (message)

#Variable Rules
# -Can contain letters, numbers, underscore
# -Cannot start with a number
# -NO spaces, use underscore
# -Names should be short and descriptive
name = "Ada Lovelace"
print (name.title())
# .title() is a method that performs and action on a piece of data. Always followed by parenthesis

# String Methods
# .upper() will make all uppercase
print (name.upper())
# .lower() will make all lowercase
print (name.lower())

# Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())
print("Hello, " + full_name.title())\

# Escaping Strings
# When you want python to interpret a string differently

# Whitespace
# To add a tab: (use \t)
print("\tPython")
# To add a new line: (use \n)
print ("Hey there" "\nHandsome")
# To strip whitespace: use (.rstrip) method
# .lstrip() for to clear left space

# Integers-- whole numbers
# Arithmetic Operators
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Python supports oder of operations! Careful
print (2 + 3)
print (5 * 4)

# Floats - Any number with a decimal

#Complex Numbers
# fairly advanced, used for imaginary numbers

# Boolean
# One of two values, True or False
