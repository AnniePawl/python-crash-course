## The Basics 
The easiest way to get python program to communicate with you via **print statements** and the **terminal**.<br>
`print('Hello World')`

### Variables
Variables in python are containers for storing data. Some  basic rules:
 - Can contain letters, numbers, underscore
 - Cannot start with a number
 - NO spaces, use underscore
 - Names should be short and descriptive
```python
message = "Life is Good"
print(message)
```

### String Methods
Python includes a number of built-in methods that can be used to manipulate strings.<br>
Here are a few commmon examples: 
```python
name = "Ada lovelace"
print(name.title()) # Ada Lovelace
print(name.upper()) # ADA LOVELACE
print(name.lower()) # ada lovelace 
``` 

### Concatenating Strings
Use `+` to merge/ combine strings
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # empty string for space
print("Hello, " + full_name.title())
```

### Escaping Strings
- `(\n)` adds a new line
- `(\t)` adds a new tab
- `(.rstrip)` strips right whitespace
- `(.lstrip)` strips left whitespace

### Arithmetic Operators
Python supports **order of operations**. Be careful!
- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`

### Avoiding Type Errors
Be careful when working w/ various types.<br>
Make sure to tell python how to interpret certain values!
```python 
age = 25 # type = number
name = "Linda" # type = string
message = "Happy " + str(age) + " birthday, " + name
```
