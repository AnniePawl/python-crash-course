# If statements
# Python often involves examining conditions
# If statements ecaluate is expressions are true or false
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# CONDITIONAL TESTS
# Remember that it's case sensitive!
# Checking for Eqaulity
car = 'bmw'
car == 'bmw'
# Checking for Inequality (!=)
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the Anchovies!")

# Numerical Comparisons
age = 18
age == 18

answer = 17
if answer != 45:
    print("Try again!")

# Checking Multiple Conditions
# Use 'and' & 'or' to combine conditional tests
age0 = 22
age1 = 21
age0 >= 21 and age1 >=21
age0 >= 21 or age1 >=21

# Checking if a Value is in a List
# Use 'in' keyword
friends = ['kelly','tina','barb']
'lisa' in friends
# Checking if a value in not in a List
# Use 'not' keyword
banned_users = ['gretta','garrett','gray']
user = 'maria'
if user not in banned_users:
    print(user.title() + "You have access to site")

# Boolean Expressions
# True/False conditinoal tests

# if-else statements
age = 17
if age >= 18:
    print ("You're old enough to vote!")
else:
    print("You're too young to vote")

# if-elif-else Chain
# Use this if you have more than 2 possible conditions to evaluate
# Python only executes one block in if-elif-else chain
# Tests run in order until one passes
# When a condition passes, python skips the rest
if age < 4:
    print("you get in for FREE!")
elif age < 18:
    print("Ticket costs $5")
else:
    print("Your admission is $10")
# You can use infinate elif blocks
# Just use multiple if statements if you want ot run through all the statments

# Using if statements with Lists
requested_sizes = ['small','extra-small']
for requested_size in requested_sizes:
    print("Adding these sizes to your cart")
