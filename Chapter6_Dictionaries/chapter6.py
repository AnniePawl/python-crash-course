# DICTIONARIES

# Simple Dictionary Example:
alien_0 = {'color': 'green', 'points': 5}
print (alien_0['color'])
print (alien_0['points'])
# Accessing Values in a Dictionary
# See above-- name of dictionary, key in []

# ADDING Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# MODIFYING dictionary values
# Give dictionary name, then new value for that Key
# Ex-Alien changes from gree to yellow
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
# Use dictionary to store on ekind of info about many Objects
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

# Looping through all KEYS in dictionary
for keys in user.keys():
    print(keys.title())
# Looping through Keys IN ORDER
for keys in sorted(user.keys()):
    print(keys.upper())

# Looping through all VALUES in dictionary
for values in user.values():
    print(values.title())
