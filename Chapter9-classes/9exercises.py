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
