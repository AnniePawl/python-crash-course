# Create an empty dictionary & add items to it
bagel = {}
bagel['type'] = 'poppy'
bagel['spread'] = 'cream cheese'
print(bagel)

# Use a dictionary to store info about your frind
# Print each piece of info
Rebi = {
'age': '25',
'height': '5ft 7in',
'hair_color':'dirty blonde',
'hair_length':'long',
}
Nicky = {
'age': '25',
'height':'5ft 4in',
}
print("My friend, Rebi is " + Rebi['age'] + " years old with " + Rebi['hair_length'] + " , " + Rebi['hair_color'] + " hair.")
# Add a new key-value pair
Rebi['favorite_color'] = 'teal'
print("And her favorite color is " + Rebi['favorite_color'])

favorite_numbers = {
'anna': 11,
'donny': 34,
'fode': 66
}
print(favorite_numbers)

# Make a dictionary containing 3 states and capitals
# Use a loop to print something about each state
# Use a loop to print each state (key)
# Use loop to print each capital (value)
state_capitals = {'alabama':'montgomery','arizona':'phoenix','california':'sacramento'}

for state, capital in state_capitals.items():
    print("The capital of " + state.title() + " is " + capital.title())

for key, value in state_capitals.items():
    print("Key: " + key)
    print("Value: " + value)

# Start with an empty dictionary
# Add key-value pairs to it
# Print keys and values

pets = {}
pets['anna'] = 'dog'
pets['donny'] = 'cat'
pets['fode'] = 'bird'
pets['dennis'] = 'beaver'
print(pets)
print(pets.values())
print(pets.keys())

for person, pet in pets.items():
    print(person)
    print(pet)

for person, pet in pets.items():
    print(person.title() + " has a pet " + pet + ".")

# Store a dictionary in dictionary
fruit_description = {
'banana':{'shape':'tubular','color':'yellow'},
'apple':{'shape':'round','color':'red'},
'pear':{'shape':'curvy','color':'green'},
}
# Make every fruit rainbow colored
for info in fruit_description.values():
    info['color'] = 'rainbow'
    print(info)

# Make several dictionaries, store them in a list
# Include descriptions about that animal
# Loop through and print everything you know about the animal
animal1 = {'type':'elephant','color':'grey', 'texture':'fuzzy'}
animal2 = {'type':'tiger','color':'black & orange', 'texture':'furry'}
animal3 = {'type':'bear','color':'brown','texture':'fuzzy'}
animals = [animal1, animal2, animal3]

for animal in animals:
    print(animal['type'].title() + "s are " + animal['color'].title() +  " and " + animal['texture'].title() + ".")

# Dictionary of fave places
# Loop through and print every person's fave destination
fave_places = {
'anna':'berlin',
'jeremy':'tokyo',
'donny':'kiev'
}
for key, value in fave_places.items():
    print(key.title() + " loves to visit " + value.title())

# Make dictionary called cities, create another dictionary w/ info about each
