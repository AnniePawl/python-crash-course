# DICTIONARIES
- A collection of key-value pairs
- Allow you to connect pieces of related information.
- Store any two kinds of info that can be matched up
- Python doesn't care what order key-value pairs are stored. It only tracks connections between individual keys and values

## Simple Dictionary Example:
- Key's are connected to their value with colon (:)
- Pairs are seperated by commas
- You can use key to access its  value 
```python
alien_0 = {'color': 'green', 'points': 5}
```

### Accessing Values in a Dictionary
To **add** a `key:value` pair, provide dictionary name, followed by new key in square brackets
```python
alien_0['x_position'] = 0
alien_0['y_position'] = 25
```

## Starting with an EMPTY Dictionary
Define empty dictionary and add each key-value pair on it's own line.
```python
siblings = {}
siblings['name'] = "Anna"
siblings['age'] = 25
print(siblings
)
```
## MODIFYING dictionary values
Give dictionary name with key in square brackets, then new value.
```python
alien_0 = {'color': 'green'}
message = 'This alien is ' + alien_0['color'] + '.'
print (message)

alien_0['color'] = 'yellow'
print ('This alien is now ' + alien_0['color'] + ".")

alien1 = {'color': 'green','points':5}
print(alien1)
# REMOVING Key-Value Pairs
del alien1['points']
print(alien1)
```

# Dictionary of SIMILAR OBJECTS
Use dictionary to store info about many Objects
```python
fave_languages = {
    'jen':'python',
    'lauren':'c',
    'yolanda':'ruby'
}

print (fave_languages)
print ("yolada's favorite language is " + fave_languages['yolanda'].title())
```

## LOOPING through DICTIONARY
Looping through all key-value pairs
```python
user = {
'first_name':'anna',
'last_name':'pawl',
'age':'25',
}
```
You can use any varibles
```
for key, value in user.items():
    print("\nKey: " + key)
    print("Value: " + value)
```
Could have been written like, "for k , v in user.items()"

### Looping through ALL KEYS in dictionary
- Looking through keys is default behavior when looping thry dictionary
- You can access value associated with any key
- You can use keys() method or omit it
- key() method not just for loopings, also returns 
```python
list of all keys
for keys in user.keys():
    print(keys.title())
```

### Looping through Keys IN ORDER
- Can't get items in predictable order by detault
- Used sorted() function to get copy of keys in order
```python
for keys in sorted(user.keys()):
    print(keys.upper())
```

### Looping through ALL VALUES in dictionary
- values() method returns list of values without keys
- Will pull all values without checking for repeats.
```python
for values in user.values():
    print(values.title())
# To return values WITHOUT REPEATS, use a "set"
# SET is similar to a list but each item in set must be unique
for languages in set(fave_languages.values()):
    print(languages.title())
```


## NESTING
- Nesting helps you store a set of dictionaries in a list or list of items as a value in a dictionary
- Nest a set of dictionaries in a list
- Nest a list of items inside dictionary
- Nest a dictionary inside another dictioanry

Build a list of 3 cats by creating 3 cat dictionaries
```python
cat1 = {'color':'blue', 'age':'5'}
cat2 = {'color':'red', 'age':'6'}
cat3 = {'color':'purple', 'age':'3'}

cats = [cat1, cat2, cat3]
for cat in cats:
    print(cat)
```
Use range to create 5 cats. 
Cats will have the same characteristics, but each considered a seperate object. 

```python
cats = []
for num_cats in range(5):
    new_cat = {'color':'black','age':'7','speed':'slow'}
    cats.append(new_cat)
# print(cats)
# Use slice to show the first 3 cats
for cat in cats[:3]:
# Show how many cats you've made
    print("I have " + str(len(cats)) + " cats!")

# Since each cat is a seperate object, we can modiy them individually
# Change first 2 cats to yellow and fast
for cat in cats[0:2]:
    if cat['color'] == 'black':
        cat['color'] = 'yellow'
        cat['speed'] = 'fast'
for cat in cats[0:5]:
    print(cat)
```

# LIST inside a DICTIONARY
- Nest a list inside dictionary when you want more than one value to be associated with a single key
- Don't nest lists in dictionaries too deep
```python
pizza = {
'crust': 'thick',
'toppings':['mushrooms', 'extra cheese','garlic'],
}
print("You ordered a pizzed with " + pizza['crust']+ " crust, and the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
```

### DICTIONARY in a Dictionary
Careful! Code can quickly become complicated
```python
players = {
    'apawl': {'first':'anna','last':'pawl','location':'sf'
    },
    'jpawl':{
    'first':'joey',
    'last':'pawl',
    'location':'ny'
    },
    }

for info in players.values():
    print(info)
    # should print dictionary of values
    for keys in info.keys():
        print(keys)
```

## dictionary Access
dictionary value access
```python
print(players['apawl']['first'])
print(players['bonny'])
```
# error b/c key doesnt exist
# Check dictionary key
# Accessting by key is direct yay
