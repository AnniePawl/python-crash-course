## PRINT STATEMENT
The easiest way to get python program to communicate with you via the terminal.<br>
*Dont Forget, in Python3, print statement needs parenthesis()
`print("Hello World")`

### MY FIRST VARIABLE
```python
message = "Life is Good"
print(message)
```
**Variable Rules:**
 - Can contain letters, numbers, underscore
 - Cannot start with a number
 - NO spaces, use underscore
 - Names should be short and descriptive

### STRING METHODS
```python
name = "Ada Lovelace"
print(name.title()) # transfors name to title case
print(name.upper()) # uppercases everything
print(name.lower()) # lowercases everything
``` 

### CONCATENATING STRINGS
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # remember empty space for string
print(full_name.title())
print("Hello, " + full_name.title())
```

### ESCAPING STRINGS
- `(\n)` adds a new line
- `(\t)` adds a new tab
- `(.rstrip)` strips right whitespace
- `(.lstrip)` strips left whitespace
```python
print("\tPython")
print("Hey there" "\nHandsome")
```

### WORKING WITH NUMBERS
- Integers  (Whole Numbers)
- Arithmetic Operators
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Python supports order of operations!- Careful

### AVOIDING TYPE ERRORS w/ STRINGS
Be careful when working w/ various types.
Make sure to tell python how to interpret certain values
```python 
age = 25
name = "Linda"
message = "Happy " + str(age) + " birthday, " + name
print(message)
```
