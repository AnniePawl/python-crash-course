# Numerical Lists Practice

evens = list(range(2, 11, 2))
print("Evens: " + str(evens))

odds = list(range(1, 10, 2))
print("Odds: " + str(odds))

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print("Here's a list of squares:" + str(squares))

cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
print("Here's a list of cubes:" + str(cubes))

squares = []
for value in range(1, 11):
    squares.append(value**2)
print("More squares: " + str(squares))

fours = []
for value in range(1, 11):
    fours.append(value**4)
print("Powers of 4: " + str(fours))

squares = [value**2 for value in range(1, 21)]
print("Squares of 1-20: " + str(squares))

cubes = [value**3 for value in range(1, 11)]
print("More Cubes: " + str(cubes))

girls = ['boo', 'winnie', 'bella', 'maisy', 'rocky', 'echo', 'gallagher']
print("Here are my girls: ")
for girl in girls[:3]:
    print(girl.title())

anna_colors = ['yellow', 'oragen', 'red']
anna_colors.append('green')
kats_colors = anna_colors[:]

kats_colors.append('blue')
print(anna_colors)
print(kats_colors)

# Tuples
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

fruits = ('banana', 'apple', 'bloob')
fruits = ('banana', 'apple', 'bloob', 'carrot')
print(fruits)


dogs = ['bella', 'winnie', 'boo', 'maisy']
for dog in dogs:
    print("Hi " + dog.title() + "!")

for value in range(1, 5):
    print(value)

numbers_list = list(range(1, 5))
print(numbers_list)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 10, 2))
print(odd_numbers)

numbers = [1, 4, 32, 12, 65, 43, 7]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

squares = []
for number in range(1, 11):
    square = number**2
    squares.append(square)
print(squares)


cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
print(cubes)

drinks = ['soda', 'tea', 'coffee']
for drink in drinks:
    print("I love to drink " + drink)

puppies = ['boo', 'bella', 'winnie']
for puppy in puppies:
    print(puppy.title() + " is the best")
print("My puppies rule")

# More Numerical Lists
for value in range(1, 5):
    print(value)

# Make list of numbers
numbers = list(range(1, 11))
print(numbers)

for value in range(2, 11, 2):
    print(value)

evens = list(range(2, 11, 2))
print(evens)

odds = list(range(1, 10, 2))
print(odds)

# Squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

quartic = []
for value in range(1, 11):
    quart = value ** 4
    quartic.append(quart)
print(quartic)

quintic = []
for value in range(1, 11):
    quint = value ** 5
    quintic.append(quint)
print(quintic)

# Shorthand
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)


# Simple Stats
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(numbers), max(numbers))
num_length = len(numbers)
print(num_length)
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
num_sum = sum(numbers)
print("Number sum = " + str(num_sum))

# List Comprehensions
squares = [value**2 for value in range(1, 6)]
print(squares)

cubes = [value**3 for value in range(1, 6)]
print(cubes)

quartics = [value ** 4 for value in range(1, 6)]
print(quartics)

quintics = [value ** 5 for value in range(1, 6)]

one_to_twenty = list(range(1, 21))
print(one_to_twenty)

thousand = list(range(1, 1001))
print("This is min: " + str(min(thousand)))
print("This is max: " + str(max(thousand)))
print("This is the sum: " + str(sum(thousand)))

odds_to_twenty = list(range(1, 20, 2))
print(odds_to_twenty)

threes = list(range(3, 30, 3))
print(threes)

squares = [value**2 for value in range(1, 11)]
print(squares)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# List Slicing
people = ['jon', 'jackson', 'john', 'jonathan']
print(people[0:2])
print(people[1:])
print(people[:3])
print(people[-1].title())
# Reverse list
print(people[::-1])

for person in people[0:2]:
    print(person.title() + " is cool")

# Copying a List
animals = ['cow', 'crow']
c_animals = animals[::-1]
print(c_animals)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

cubes = []
for value in range(1, 6):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

square = [value**2 for value in range(1, 6)
          ]
print(squares)

list
