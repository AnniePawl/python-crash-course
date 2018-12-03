# LOOPING THROUGH SIMPLE LISTS
a_names = ['anna','abby','arnold']
for name in a_names:
    print(name)

dogs = ['boo','winnie','maisy','georgie ']
for dog in dogs:
    print ("Aww! " + dog.title() + " is so cute!")

shoe_sizes = [8,9,10,11]
for size in shoe_sizes:
    print("We have that shoe in size " + str(size))

fruits = ['apples', 'pears','peaches']
fruits.append('strawberries')
fruits.insert(0,'star fruit')
for fruit in fruits:
    print ("Mmm! These " + fruit + " taste so good!")

breeds = []
breeds.append("wheaton")
breeds.append("golden-doodle")
breeds.append("poodle")
breeds.insert(0,"ridgeback")
print(breeds)
for breed in breeds:
    print("I have a " + breed.title())

sauces = ['tomato','clam','pesto']
for sauce in sauces:
    print ("Love my pasta with extra " + sauce)

toppings = ['garlic','basil','olive oil']
for topping in toppings:
    print("I love my pasta with extra " + topping)
print("Wow I love pasta!")

b_words = ['bamboo','bunny','bukly']
print("Here are some words that start with the letter 'B':")
for b in b_words:
    print(b.title() + " starts with 'B'")


# LISTS AND NUMBERS
# Use a loop to PRINT 1-10 (inclusive)
one_ten = []
for value in range(1,11):
    one_ten.append(value)
print(one_ten)
# LIST COMPREHENSION
one_five = [value for value in range(1,6)]
print(one_five)

# EVEN NUMS 1-10
even = list(range(2,11,2))
print (even)

# ODD NUMS 1-10
odds = list(range(1,10,2))
print (odds)

# print SQUARES of 1-10
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# print squares from 10-20
big_squares = []
for num in range(10,21):
    square = num**2
    big_squares.append(square)
print(big_squares)

# print CUBES of 1-10
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(value)
print(cubes)

# CUBES LIST COMPREHENSION
cubes = [value**3 for value in range(1,11)]
print(cubes)

# MIN, MAX, SUM
ha = [1,5,8,2,4,56,4,5,98,7,6,1,]
print(min(ha))
print(max(ha))
print (sum(ha))

# Same thing, but initialize empty list
numbers = []
for values in range(1,21):
    numbers.append(values)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# List multiples of 3 until 30
mults_of_three = list(range(0,31,3))
print(mults_of_three)
# Use a for Loop
for three in threes:
    print(three)

# Make a list of first 10 cubes
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)
# Use List Comprehension for cube list
cubes = [value**3 for value in range(1,11)]
print(cubes)

# Create a list, print part of it
friends = []
friends.append('clara')
friends.append('emma')
friends.append('ellie')
friends.append('caroline')
print(friends[1].title())
print("These are my friends:")
for friend in friends:
    print(friend.title())

# Make a simple list, Make a copy
office = []
office.append('hole punch')
office.append('paper')
office.append('pencil')
home_office = office[:]
print(home_office)

# Make longish list
# Print 1st two, then last 3 two items + a message
furniture = ['chair','sofa','table','desk','lamp','dresser','stool']
print (furniture)
print (furniture[1:3])
print ("I own all these: ")
for item in furniture:
    print(item.title())
print ("That's a lot, right!?")

fancy_furniture = furniture[:]
print(fancy_furniture)
fancy_furniture.append('cabinet')
print(fancy_furniture)
print(furniture)

# Make a tuple and access some elements
dimensions = (200,100)
print(dimensions[1])
# Write over the tuple
dimensions = (50,50)
print(dimensions[1])

# Make a basic Tuple
# Replace two items by rewriting tuple
# Use for loop to print new tuple
food_tuple = ('cabbage','lettuce','beer','oreos','carrots')
food_tuple = ('cabbage','lettuce','beer','milk','beets')
print("I need the following items from the grocery store, Tom")
for food in food_tuple:
    print(food.title())
print("Call if you have any questions")


# More Num Practice
numbers = list(range(0,5))
print(numbers)

squares = []
for values in range(1,11):
    square = values**2
    squares.append(square)
print(squares)

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

digits = [2,6,4,1,7,4,22,5,4,9,77,3]
print(max(digits))

squares =  []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# Squares List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)

cubes = []
for value in range (1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)
# Cubes List Comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)

odds = list(range(1,11,2))
print(odds)

# print numbers 10-20
for value in range(10,21):
    print(value)
num1_20 = list(range(10,21))
print(num1_20)

digits = [3,5,66,44,5,67,54,7]
print(max(digits))
print(min(digits))
print(sum(digits))
print(sorted(digits))

cubes = [value**3 for value in range(1,11)]
print(cubes)

# Slicing Practice
flavors = ['grape','stawberry','watermelon','lemon']
flavors.insert(1,'pineapple')
print(flavors)
print(flavors[0:2])
print(flavors[:3])
print(flavors[1:])
# Loop through a slice
print("my favorite flavors are: ")
for flavor in flavors [:3]:
    print(flavor.title())
# Copy a List
fave_flavors = flavors[:]
fave_flavors.append('cranberry')
del fave_flavors[1]
fave_flavors.pop(3)
fave_flavors.remove('watermelon')
print(fave_flavors)
