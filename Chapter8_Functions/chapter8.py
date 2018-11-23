#FUNCTIONS

# Simplest FUNCTION STRUCTURE
# Define it, call it at the bottom
def greet_user():
    """Display  a simple greeting."""
    print("hi!")

greet_user()

# Passing Information to a Function
# Adding username allows function to accept any value of username each time you call it.
def invitation (name):
    print("Hey, " + name.title()+ "You're a super star!")

invitation("Jess")

# Arguments and Parameters
# When you call a func, python must match each argument in call with parameter in func def

# Passing Arguments (Positional and Keyword)
# Func defs can have multiple parameters, so function call might need multiple arguments

# POSITIONAL ARGUMENTS  (Order Matters)
# Must be in same order that parameters were written
def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Multiple Function Calls
# You can call a function as many times as needed
# Describing a second pet just requires one more call
# Add this line to the bottom:
describe_pet('butterfly','betsy')

# KEYWORD ARGUMENTS   (Order Doesn't Matter)
# Each consists of var name and value; and lists and dictionaries of values
# Directly associate name and value in argument
# Free you from worrying about correctly ordering arguments
describe_pet(animal_type = 'bug', pet_name = 'bonny')

# DEFAULT values
# You can define a default value for each parameter
# Py will use default unless argument in function call
# def describe_pet(pet_name, animal_type ='dog')
# CAREFUL about positioning! Put defaults at the end so python can interpret positional arguments correctly

 #EQUIVALENT FUNCTION CALLS
 # Several ways to call a function! Can use different styles
# A cat named Charles
describe_pet('charles')
describe_pet(pet_name = 'charles')
# A horse named Henrietta
describe_pet ('henrietta','horse')
describe_pet (pet_name = 'henrietta', animal_type = 'horse')
describe_pet (animal_type = 'horse',pet_name = 'henrietta')

# AVOIDING ARGUMENT ERRORS
# Unmatched Arguments -- when you provide fewing or more arguments than necessary

# RETURN VALUES  - the value that functions return
# Allow you to move a lot of work into functions
