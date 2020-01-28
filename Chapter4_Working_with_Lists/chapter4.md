## Working with Lists 

### Looping
- Looping is the most common way to automate repetitive tasks.
- Allows you to perform same task on each item
- INDENTATION is key. Everything indented after for/in statement is considered in the loop
- Non-indented code will only be executed once

```python
dogs = ['boo','meli','winnie','zola']
for dog in dogs: # takes item from dogs adn stores in 'dog' variable
    print("My dog's name is " + dog.title())
```

```python
magicians = ['sabrina','becky','leonardo']
for magician in magicians:
    print("Hi " + magician.title() + ", you did great!")
print("Thanks everyone, that was a great show!") # unindented --> prints 1x
```

### Numerical Lists, Range Function()
- Use `range()` to make a list of numbers: `range(1,6)` returns 1,2,3,4,5
- Remember **off-by-one** principal b/c index 0
- wrap `range()` in `list()` to create list: `nums = list(range(1,5))`
```python
# First value = starting value
# Second value = ending val (off by one)
# Last value = interval 
even_numbers = list(range(2,11,2)) 
odd_numbers = list(range(1,10,2))
```

### Simple Stats (Min and Max functions)
```python
digits = [3,55,64,73,25,1,87,66,140,31,17,3,86]
print(min(digits))
print(max(digits))
print(sum(digits))
```

### Squares and Cubes
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

## List Comprehensions
Allow you to create a lot of functionality in one line of code. Combines "for loop" and creation of new elements
```python
squares = [value**2 for value in range(1,11)]

cubes = (value**3 for value in range(1,11))
```

## Working w/ Part of a List
**Slicing:**
 - Slice a list to work with a subset
 - Specify index of 1st & last elements you want to work w/
- Remember 'one-off' behavior
- If you don't specify 1st index, default start at 0
- If you don't specify 2ns index, will print until last num
- Use negative num to print from end of list
   
```python
green_stuff = ['grass','lime','granny smith','olive']
print(green_stuff[:2]) #prings first 2 items
print(green_stuff[0:]) # prints all items
print(green_stuff[-3:]) # prints last 3 items 
```

**Looping Thru Slice**
```python
players = ['john','jim','jerry','jenny','jess']
print("Here are the players on my team: ")
for player in players[1:]:
    print(player.title())
```

**Copying a List** <br>
You can make a slice that includes entire original list by omitting first and second index([:]). This tells python to make a slice that starts at first item and ends at lastself.
```python
anna = ['tall','pretty','smart']
twin = anna[:]
twin.append('clever')
```

# TUPLES
- Simple data structure
- Looks like lists, but with parenthesis `( )`
- Allow you to create list of items that can't change, **immutable**
- If you try to change a value, you'll get an ERROR
- Must redefine tuple value to change it'''

```python
dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 won't work, can't overwrite like this
```
**Looping thru Tuple Values**
```python
for dimension in dimensions:
    print(dimension)
```

**Rewriting Tuple** 
- Cannot 'modify' a tuple
- CAN assign new value to variable holding tuple
```python
dimensions = (200, 50)
print("Original Dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (500, 500) # Must redefine tuple to change
print("\n Modified Dimentions: ")
for dimension in dimensions:
    print(dimension)
```
