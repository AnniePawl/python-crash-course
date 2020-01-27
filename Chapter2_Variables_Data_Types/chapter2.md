# The Basics 
### Print Statement
The easiest way to get python program to communicate with you via the terminal.<br>
In **Python3**, print statement needs parenthesis`( )` <br>
Example: `print('Hello World')`

## Variables
 - Can contain letters, numbers, underscore
 - Cannot start with a number
 - NO spaces, use underscore
 - Names should be short and descriptive
```python
message = "Life is Good"
print(message)
```

## String Methods
Python includes a number of built-in methods that can be used to manipulate strings.<br>
Here are a few commmon examples: 
```python
name = "Ada Lovelace"
print(name.title()) # transforms name to title case
print(name.upper()) # uppercases everything
print(name.lower()) # lowercases everything
``` 

## Concatenating Strings
Use `+` to merge/ combine strings
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # remember empty space for space
print(full_name.title())
print("Hello, " + full_name.title())
```

## Escaping Strings
- `(\n)` adds a new line
- `(\t)` adds a new tab
- `(.rstrip)` strips right whitespace
- `(.lstrip)` strips left whitespace
```python
print("\tPython")
print("Hey there" "\nHandsome")
```

## Working with Numbers
**Arithmetic Operators** can be used to manipulate numbers <br>
Python supports **order of operations**. Be careful!
- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`

## Avoiding Type Errors
Be careful when working w/ various types.<br>
Make sure to tell python how to interpret certain values!
```python 
age = 25 #Type=number
name = "Linda" #Type=string
message = "Happy " + str(age) + " birthday, " + name
print(message)
```
