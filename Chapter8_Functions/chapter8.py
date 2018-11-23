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
# describe_pet('charles')
# describe_pet(pet_name = 'charles')
# A horse named Henrietta
describe_pet ('henrietta','horse')
describe_pet (pet_name = 'henrietta', animal_type = 'horse')
describe_pet (animal_type = 'horse',pet_name = 'henrietta')

# AVOIDING ARGUMENT ERRORS
# Unmatched Arguments -- when you provide fewing or more arguments than necessary

# RETURN VALUES  - the value that functions return
# Allow you to move a lot of work into functions
def get_formatted_name(first_name, last_name):
    '''return full name, neatly'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# Making an Argument Optional
# Sometimes helpful so people using func can choose to provide extra info only if they want to
# Examlple: Optionally enter middle name

def get_formatted_name(first_name, middle_name, last_name):
    full_name =  first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jonh','lee','hooker')
print(musician)
# To make a value optional, give argument an empty default value
# Set middle name default value to empty string and move to end of parameter list
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name =  first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

person = get_formatted_name('gretta','henderson')
print(person)

person = get_formatted_name('betsy','boop')
print(person)
