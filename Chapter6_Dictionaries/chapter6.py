# DICTIONARIES
# A collection of key-value pairs
# Allow you to connect pieces of related information.
# Store any two kinds of info that can be matched up
# Python doesn't care what order key-value pairs are stored. It only tracks connections between individual keys and values

# Simple Dictionary Example:
# Key's are connected to their value with colon (:)
# Pairs are seperated by commas
alien_0 = {'color': 'green', 'points': 5}
print (alien_0['color'])
print (alien_0['points'])
# You can use a key to access value associated with it later

# Accessing Values in a Dictionary
# ADDING Key-Value Pair
# Give dictionary name, followed by new key in square brackets
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an EMPTY Dictionary
# Define empty dictionary and add each key-value pair on it's own line.
siblings = {}
siblings['name'] = "Anna"
siblings['age'] = 25
print(siblings
)
# MODIFYING dictionary values
# Ex-Alien changes from green to yellow
# Give dictionary name with key in square brackets, then new value.
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

# Dictionary of SIMILAR OBJECTS
# Use dictionary to store info about many Objects
fave_languages = {
    'jen':'python',
    'lauren':'c',
    'yolanda':'ruby'
}

print (fave_languages)
print ("yolada's favorite language is " + fave_languages['yolanda'].title())

# LOOPING through DICTIONARY
# Looping through all key-value pairs
user = {
'first_name':'anna',
'last_name':'pawl',
'age':'25',
}
# You can use any varibles
for key, value in user.items():
    print("\nKey: " + key)
    print("Value: " + value)
#  Could have been written like, "for k , v in user.items()"

# Looping through ALL KEYS in dictionary
# Looking through keys is default behavior when looping thry dictionary
# You can access value associated with any key
#  Keys()
# You can use keys() method or omit it
# key() methos not just for loopings, also returns list of all keys
for keys in user.keys():
    print(keys.title())

# Looping through Keys IN ORDER
# Can't get items in predictable order by detault
# Used sorted() function to get copy of keys in order
for keys in sorted(user.keys()):
    print(keys.upper())

# Looping through ALL VALUES in dictionary
# values() method returns list of values without keys
# Will pull all values without checking for repeats.
for values in user.values():
    print(values.title())
# To return values WITHOUT REPEATS, use a "set"
# SET is similar to a list but each item in set must be unique
for languages in set(fave_languages.values()):
    print(languages.title())


# NESTING
# Nesting helps you store a set of dictionaries in a list or list of items as a value in a dictionary
# Nest a set of dictionaries in a list
# Nest a list of items inside dictionary
# Nest a dictionary inside another dictioanry

# Build a list of 3 cats by creating 3 cat dictionaries
cat1 = {'color':'blue', 'age':'5'}
cat2 = {'color':'red', 'age':'6'}
cat3 = {'color':'purple', 'age':'3'}

cats = [cat1, cat2, cat3]
for cat in cats:
    print(cat)

# A bigger example: Use range to create 5 cats
cats = []
# Cats will have the same characteristics, but each considered a seperate object
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


# LIST inside a DICTIONARY
# Nest a list inside dictionary when you want more than one value to be associated with a single key
# *** Don't nest lists in dictionaries too deep
pizza = {
'crust': 'thick',
'toppings':['mushrooms', 'extra cheese','garlic'],
}
print("You ordered a pizzed with " + pizza['crust']+ " crust, and the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# DICTIONARY in a Dictionary
# ** Careful! Code can quickly become complicated
players = {
    'apawl': {
    'first':'anna',
    'last':'pawl',
    'location':'sf'
    },
    'jpawl':{
    'first':'joey',
    'last':'pawl',
    'location':'ny'
    },
    }
