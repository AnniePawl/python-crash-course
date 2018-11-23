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

# RETURNING A DICTIONARY
# Functions can return more complex data structures like lists and dictionaries

def build_person(first_name, last_name):
    '''return dict of info re person'''
    person = {'first':first_name, 'last':last_name}
    return person

super_person = build_person('fiona','gallagher')
print(super_person)

# USING A FUNCTION WITH A WHILE LOOP
# *Don't forget a quit condition or loop is infinite
'''while True:
    print("\nPlease tell me your name: ")
    print("(enter'q' at anytime to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name,l_name)
print("\nHello " + formatted_name + '!')
'''

# PASSING A LIST
# When you pass list into function, func gets direct access to contents of list
def greet_users(names):
    '''print simple greeting to each listed user'''
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hanna','barb','sally']
greet_users(usernames)

# MODIDYING A LIST IN A FUNCTION
# function can modify a list, and changes are permanent

unprinted_designs = ['i phone case','robot pin','puppet']
completed_models = []

# Simulate printing each design until none are left
# Move each to completed_models post printing

# This example doesn't use functions ....
while unprinted_designs:
    current_design = unprinted_designs.pop()

    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

# Example above(WITH FUNCTIONS)
def print_models(unprinted_designs, completed_models):
    '''simulate printing each design
    Move design to completed_models after printing'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        '''simulate creating 3d print from design'''
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''show all models that were printed'''
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','barbie pendant']

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# PREVENTING FUNC FROM MODIFYING A LIST
# Send COPY OF A LIST to a function like this:
'''function_name(list_name[:])'''

# PASSING ARBITRARY NUMBER OF ARGUMENTS
# Sometimes you don't know ahead of time how many arguments your function needs
def make_pasta(*sauces):
    print(sauces)
make_pasta('tomato')
make_pasta('pesto','tomato','clam')
# We can replace print statement with loop that runs through sauces and descibes each pasta dish being ordered
def make_pasta(*sauces):
    print("\nMaking pasta with the following sauces")
    for sauce in sauces:
        print("- " + sauce)

make_pasta('pesto','tomato','clam')
make_pasta('tomato')

# Mixing POSITIONAL & ARBITRARY Arguments
# Parameter that accepts arbitrary num of arguments should be placed last in fucnion def
def make_pasta(size, *sauces):
    print("\nMaking a " + str(size) + " inch bowl of pasta with the following sauces: ")
    for sauce in sauces:
        print("- " + sauce)

make_pasta(4, 'pesto','tomato','clam')
make_pasta(5, 'tomato')

# USING ARBITRARY KEYWORD arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
