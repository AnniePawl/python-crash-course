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
