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
