# Sort the names of some friends.
# Print each name by accessing each element one at a time
my_friends = ['Rebi', 'Sarah', 'Nicky', 'Grace']
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])
print(my_friends[3])

yellow_stuff = []
yellow_stuff.append('banana')
yellow_stuff.append('daisy')
yellow_stuff.append('ped Xing sign')
print(yellow_stuff[0].title())
print(yellow_stuff[-1].title())
print("I have 3 " + yellow_stuff[0] + "s in my bag.")

# Add stuff to an Empty List
# Then delete some of the stuff
empty = []
empty.append("Apples")
empty.append("Oranges")
empty.append("Bread")
print(empty)
print(empty[1])
empty[1] = "Milk"
print(empty[1])
empty.append("Eggs")
empty.append("Cheese")
print(empty)
del empty[0]
print(empty)
# Use pop(), show that you can still access popped item
popped = empty.pop()
print(popped)

bugs = []
bugs.append('beetle')
bugs.append('lady bug')
bugs.append('mosquito')
print(bugs)

bugs[0] = 'moth'
bugs[-1] = 'ant'
print(bugs)

bugs.insert(0, 'ladybug')
bugs.insert(1, 'fly')
bugs.insert(1, 'dragonfly')
print(bugs)

del bugs[0]
del bugs[1]
print(bugs)

my_bug = bugs.pop(0)
print("My favorite bug is the " + my_bug)
print(bugs)

bugs.remove('moth')
bugs.remove('ant')
print(bugs)

# Send a greeting to friends in your list
message = "I'm so into you"
print('Hey, ' + my_friends[1] + "! You look amazing")
print('Hey, ' + my_friends[2] + "! You look amazing")
print(my_friends[0] + " " + message)

# Make a list of modes of transportation
# Use the list to make a seriesof statements about these items
transport_modes = ['bike', 'car', 'motorcycle', 'scooter']
message = "I would love to own a " + transport_modes[0] + " or a " + transport_modes[1] + \
    " but definitely neither a " + \
    transport_modes[2] + " nor a " + transport_modes[3]
print(message)

# More Practice
utensils = ['spoon', 'fork', 'knife']
print("My favorite utensil is the " + utensils[0] + ". But I also love using " +
      utensils[1] + " . In no world would I ever use a " + utensils[-1])

# Make a list w/3 people. Use list to print a message to each person
guest_list = ['Nancy', 'Gary', 'Donna', 'Ted']
invitation = "Hello, most beloved " + \
    guest_list[0] + ". Please meet at the peir for an evening of gourmet pizza."
print(invitation)
# Print statement with name of guest that can't make it. Replace guest with a new invite
print(guest_list[3] + " can\'t make it")
del guest_list[3]
guest_list.insert(3, 'Anita')
print(guest_list)
# Print how many peple are coming using len()
print("There are " + str(len(guest_list)) + " guests coming tonight!")

# Favorite candies. Replace some, add some, remove some.
candy = ['starbust', 'twix', 'snickers']
candy_message = "I'm dying for some " + candy[1].title() + " tonight."
print(candy_message)
# Replace starbust with jaw breakers
candy[0] = 'jaw breakers'
print(candy)
# Joey gave me sour straws
candy.append('sour Straws')
# Kat ate all my twix (use del)
del candy[1]
print(candy)
# Rebi snuck some bubble gum in there
candy.insert(1, 'bubble gum')
print(candy)
# Mom ate all my snickers (use pop method)
candy.pop(2)
print(candy)

# More List Practice
fruit_list = ['apples', 'oranges', 'pears']
print(fruit_list[-1].upper())
print("I've always liked " + fruit_list[1].title()
      + " the best!")
fruit_list[1] = 'strawberries'
print("How many " + fruit_list[1] + " can I have?")

animals = ['birds', 'turles', 'dogs']
print("i love " + animals[1])
animals[1] = 'cats'
print("I love " + animals[1])
animals.append('cats')
print(animals)


# SORTING PRACTICE
# Make a list of places to visit
# Find the length of the list
# Use sorted() method to put in alphabetical order (temp)
# Use sorted () to print in reverse alphabetical order (temp)
places_to_see = ['toronto', 'amsterdam', 'toyko', 'budapest']
print(places_to_see)
print(len(places_to_see))
print(sorted(places_to_see))
print(places_to_see)
places_to_see.sort()
print(places_to_see)
places_to_see.reverse()
print(places_to_see)
places_to_see.reverse()
places_to_see.sort()
print(places_to_see)

# More Sorting Practice
# Permanently sort and revsere sort
b_words = []
b_words.append("butter")
b_words.append("bronco")
b_words.append("buzzer")
b_words.append("bbq")
print(b_words)
b_words.sort()
print(b_words)
b_words.sort(reverse=True)

# Temporarily sort a list
r_words = ['ride', 'rhino', 'ribbon', 'red', 'rainbow']
print(sorted(r_words))

# Print list in Reverse
r_words.reverse()
print(r_words)

to_visit = ['sydney', 'milan', 'cairo']
to_visit.sort(reverse=True)
print(to_visit)

to_eat = ['berry', 'toast', 'cracker']
print(sorted(to_eat))
to_eat.reverse()
print(to_eat)
print(len(to_eat))

# More Practice
pens = ['ball point', 'fountain', 'gel']
print(pens[0].title())
print(pens[1].title())
print(pens[2].title())

for pen in pens:
    print("I love " + pen + " pens")

print(pens[0].title() + " are my favorite")

monsters = []
monsters.append('goblin')
monsters.append('vampire')
monsters.append('devil')
print(monsters)
print(monsters[0].title())
monsters[0] = 'fire ball'
print(monsters)
monsters.insert(0, 'grizzly square')
print(monsters)
monsters.insert(1, 'charmander')
print(monsters)
del monsters[1]
print(monsters)
monsters.pop(1)
popped_monsters = monsters.pop()
print(popped_monsters)
print(monsters)
monsters.remove('vampire')
print(monsters)

jam = ['raspberry', 'blueberry', 'strawberry']
jam[0] = 'apple'
print(jam[-1])
jam.append('current')
print(jam)
jam.insert(1, 'banana')
jam.insert(1, 'carrot')
print(jam)
del jam[0]
# jam.pop()
# jam.remove('banana')
# jam.sort()
# jam.sort(reverse=True)
print(sorted(jam))
print(jam)
print(len(jam))

# More PRACTICE

m_words = []
m_words.append('math')
m_words.append('monarchy')
m_words.append('monkey')
m_words.append('morning')
m_words.append('mushroom')
print(m_words)
print(m_words[-2])

m_words.remove('morning')
m_words.remove('monkey')
print(m_words)

m_words.insert(0, 'mullberry')
m_words.insert(1, 'mushy')
m_words.insert(-1, 'mustard')
print(m_words)

del m_words[0]
print(m_words)

m_words.sort()
print(m_words)
m_words.sort(reverse=True)
print(m_words)

p_words = []
p_words.append('pickle')
p_words.append('pinecone')
p_words.insert(0, 'possum')
p_words.insert(1, 'portrait')
p_words.insert(2, 'prickly')
print(p_words)

p_words.remove('portrait')
p_words.remove('possum')
print(p_words)

p_words.append('plantain')
p_words.append('pizza')
p_words.insert(1, 'poo')
p_words.insert(0, 'prince')
print(p_words)

del p_words[0]
del p_words[-1]
print(p_words)

print(sorted(p_words))
print(p_words)

p_words.sort()
print(p_words)

p_words.sort(reverse=True)
print(p_words)

print(len(p_words))
print(len(m_words))

print(p_words)
p_words.reverse()
print(p_words)

drinks = ['soda', 'slushie', 'coke', 'sprite',
          'latte', 'coffee', 'chai', 'tea']

drinks.reverse()
drinks.sort()
drinks.sort(reverse=True)

print(sorted(drinks))

names = ['anna', 'annabelle', 'arabella']
furniture = ['chair', 'sofa',  'couch',  'table', 'desk', 'bed']
print(furniture[1].title())
print(furniture[-1].upper())
print(names[-1].title() + " loves to buy " + furniture[0] + "s.")

# Modifying List
birds = ['robin', 'pigeon', 'seagull']
birds[0] = 'cardinal'
print(birds)
birds.append('robin')
print(birds)
birds.insert(1, 'owl')
print(birds)
del birds[0]
print(birds)

jams = ['strawberry', 'peach', 'blueberry']
popped_jams = jams.pop()
print(popped_jams)
latest_jam = jams.pop()
print("The latest jam I made is " + latest_jam.title() + " jam")

greetings = []
greetings.append('hi')
greetings.append('bye')
greetings[0] = 'gretta'
print(greetings)
greetings.insert(0, 'hi')
print(greetings)
del greetings[1]
print(greetings)
greetings.insert(-2, 'later')
print(greetings)
greetings.pop()
print(greetings)
greetings.append('goodbye')
print(greetings)
greetings.remove('goodbye')
print(greetings)

# Organizing List
cars = ['bmw',  'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

candy = ['skittles', 'twizzlers', 'gummies']
print(sorted(candy))
print(candy)

clothes = ['shirt', 'pants', 'bra']
clothes.reverse()
print(clothes)
print(len(clothes))

states = ['colorado', 'texas', 'alabama', 'washington', 'florida']
sorted_states = sorted(states)
print(sorted_states)
print(states)
states.sort(reverse=True)
print(states)

drinks = ['soda', 'tea', 'coffee']
print(drinks)
del drinks[0]
print(drinks)
drinks.remove('tea')
print(drinks)
drinks.append('tea')
drinks.insert(-1, 'soda')
print(drinks)
reversed_drinks = sorted(drinks, reverse=True)
print(reversed_drinks)

cats = ['carol', 'aaron', 'betsy']
alphabetical_cats = sorted(cats)
print(alphabetical_cats)
backwards_cats = sorted(cats, reverse=True)
print(backwards_cats)

dogs = ['winnie', 'boo', 'bella']
dogs.sort(reverse=True)
print(dogs)

letters = ['c', 'a', 'b']
print(sorted(letters))
print(sorted(letters, reverse=True))
letters.sort(reverse=True)
print(letters)
