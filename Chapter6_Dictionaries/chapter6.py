# DICTIONARIES

# Simple Dictionary Example:
alien_0 = {'color': 'green', 'points': 5}
print (alien_0['color'])
print (alien_0['points'])
# Accessing Values in a Dictionary
# See above-- name of dictionary, key in []

# Adding Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying dictionary values
# Give dictionary name, then new value for that Key
# Ex-Alien changes from gree to yellow
alien_0 = {'color': 'green'}
message = 'This alien is ' + alien_0['color'] + '.'
print (message)

alien_0['color'] = 'yellow'
print ('This alien is now ' + alien_0['color'] + ".")


# Removing Key-Value Pairs
