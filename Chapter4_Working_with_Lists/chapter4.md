## LOOPING through and ENTIRE LIST
- Looping is the most common way to automate repetitive tasks.
- Allows you to perform same task on each item
- INDENTATION is key. Everything indented after for/in statement is considered in the loop
- Non-indented code will only be executed once

```python
dogs = ['boo','meli','winnie','zola']
for dog in dogs:
    print("My dog's name is " + dog.title())
```

- Line 2 tells python to pull a name from magicians and store it in a variable called, magician
```python
magicians = ['sabrina','becky','leonardo']
for magician in magicians:
    print("Hi " + magician.title() + ", you did great!")
print("Thanks everyone, that was a great show!")
```

## NUMERICAL LISTS w/ RANGE FUNCTION
- This will print 1 2 3 and 4 (one-off)
for value in range(1,5):
    print(value)
- You can use Range to Make a LIST OF NUMBERS
- wrap list() outside of range()
numbers = list(range(1,5))

- List the EVEN NUMBERS BETWEEN 1 and 10, then odd
```python
even_numbers = list(range(2,11,2))
print(even_numbers)
odd_numbers = list(range(1,10,2))
print(odd_numbers)
```

### Simple Stats (MIN and MAX functions)
```python
digits = [3,55,64,73,25,1,87,66,140,31,17,3,86]
print(min(digits))
print(max(digits))
sum = sum(digits)
print(sum)
```

#### Create a list of the FIRST TEN SQUARED NUMBERS
```python
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
```

```python 
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)
```

## LIST COMPREHENSIONS
Allow you to create a lot of functionality in one line of code. Combines "for loop" and creation of new elements
```python
squares = [value**2 for value in range(1,11)]
print(squares)
```

### WORKING w/ PART OF A LIST
# SLICING
 - Slice a list to work with a subset
    - Specify index of 1st & last elements you want to work w/
    - Remember 'one-off' behavior
    - If you don't specify 1st index, default start at 0
    - If you don't specify 2ns index, will print until last num
    - Use negative num to print from end of list
   
```python
green_stuff = ['grass','lime','granny smith','olive']
print(green_stuff[:2])
print(green_stuff[0:])

# This will print last 3 items in the list
print(green_stuff[-3:])

# LOOPING through a SLICE
# You can use "for loop" on list subset
players = ['john','jim','jerry','jenny','jess']
print("Here are the players on my team: ")
for player in players[1:]:
    print(player.title())
```

# COPYING A LIST
You can make a slice that includes entire original list by omitting first and second index([:]). This tells python to make a slice that starts at first item and ends at lastself.
```python
anna = ['tall','pretty','smart']
twin = anna[:]
twin.append('clever')
print(anna)
print(twin)
```

# TUPLES
- Simple data structure
- Looks like lists, but with parenthesis()
- Allow you to create list of items that can't change
- Items in tuple are called 'immutable
- If you try to change a value, you'll get an ERROR
- Must redefine tuple value to change it'''

```python
dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 won't work, can't overwrite like this
```

### LOOPING through TUPLE VALUES
```python
for dimension in dimensions:
    print(dimension)
```

### WRITING OVER A TUPLE
''' - Can't 'modify' a tuple
    - CAN assign new value to variable holding tuple
'''
### To CHANGE VALES rectangle dimensions, REDEFINE entire tuple
```python
dimensions = (200, 50)
print("Original Dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (500, 500)
print("\n Modified Dimentions: ")
for dimension in dimensions:
    print(dimension)
```
