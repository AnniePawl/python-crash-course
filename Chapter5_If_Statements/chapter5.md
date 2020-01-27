# IF STATEMENTS
''' - Python often involves examining conditions
    - Conditional Tests allow you to check conditions and respond appropriately
    - Python examines in term of True or False (boolean)'''

# SIMPLE CONDITIONAL
```python
cars = ['audi','bmw','toyota','acura']
for car in cars:
    if car  == 'bmw':
        print (car.upper())
    else:
        print(car.title())
```

# CONDITIONAL TESTS
# Remember that it's case sensitive!
# Checking for Eqaulity
# This sets car equal to bmw
car = 'bmw'
# This asks if car is bmw
car == 'bmw'
# Checking for Inequality (!=)
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the Anchovies!")

# Numerical Comparisons
# Use single space around comparison operators
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
# Often used to keep track of certain conditions, like if a game is running or not

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
# *Just use multiple if statements if you want ot run through all the statments
```python
herbs = ['basil','mint','sage']
if 'basil' in herbs:
    print("I have basil!")
if 'mint' in herbs:
    print("I have mint!")
if 'sage' in herbs:
    print("I have sage!")
```

# Using if statements with LISTS
# You can watch for special values that need to be treated differently
# You can manage chacking conditions efficiently
requested_sizes = ['small','extra-small','medium']
for requested_size in requested_sizes:
# What if the store runs out of smalls!?
```python
    if requested_size == 'small':
        print("Sorry! We're out of smalls...")
    else:
        print("Adding " + requested_size + " to your cart!")
```

# Check if a list is not empty
# When the name of a lsit is used in an if statement, python returns true if the list contains atleast 1 item. Otherwise, its false
```python
toppings = ['sprinkles']
if toppings:
    for topping in toppings:
        print("Adding " + topping)
```

# Using Multiple Lists
# You can use lists and if statements to make sure your input makes sense before acting on it
# Check list of available toppings against requested toppings
```python
available_toppings = ['sprinkles','fudge']
requested_toppings = ['sprinkles','ants']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry we don't have " + requested_topping)
```
