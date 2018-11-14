# Sort the names of some friends.
# Print each name by accessing each element one at a time
my_friends = ['Rebi','Grace','Nicky','Clara']
print (my_friends[0])
print (my_friends[1])
print (my_friends[2])
print (my_friends[3])

siblings = ['joey','kathyrn']
print (siblings[0].title())

# Text each friend. Text should be the same, but personalized with person's names
message = 'Hey, ' + my_friends[2] +"! You look super good"
print (message)

# Make a list of modes of transportation
# Use the list to make a seriesof statements about these items
transport_modes = ['car','bike','motorcycle','scooter']
message = "I would like to own a " + transport_modes[0] + " or maybe a " + transport_modes[1] + " but definitely neither a " + transport_modes[2] + " nor a " + transport_modes[3]
print (message)

# More Practice
utensils = ['fork', 'spoon', 'knife']
print (utensils[1].title())
print ("My favorite utensil is hands down the " + utensils[0].title() + ". But I'm also a big fan of the " + utensils[1].title() + " if I'm being perfectly honest.")

# Make a list w/3 people. Use list to print a message to each person
guest_list = ['Nancy','Gary','Donna','Ted']
invitation = "Hello, most beloved " + guest_list[0] + ". Please meet at the peir for an evening of gourmet pizza."
print (invitation)
# Print statement with name of guest that can't make it. Replace guest with a new invite
print (guest_list[3] + " can\'t make it")
del guest_list[3]
guest_list.insert(3, 'Anita')
print (guest_list)
# Print how many peple are coming using len()
print ("There are " + str(len(guest_list)) + " guests coming tonight!")


# List Favorite candies. Replace some, add some, remove some.
candy = ['starbust', 'twix','snickers']
candy_message = "I'm dying for some " + candy[1].title() +  " tonight."
print (candy_message)
# Replace starbust with jaw breakers
candy[0] = 'jaw breakers'
print (candy)
# Joey gave me sour straws
candy.append('sour Straws')
# Kat ate all my twix (use del)
del candy[1]
print (candy)
# Rebi snuck some bubble gum in there
candy.insert(1,'bubble gum')
print (candy)
# Mom ate all my snickers (use pop method)
candy.pop(2)
print (candy)

# Make a list of places to visit
# Find the length of the list
# Use sorted() method to put in alphabetical order (temp)
# Use sorted () to print in reverse alphabetical order (temp)
places_to_see = ['toronto', 'amsterdam', 'toyko', 'budapest']
print (places_to_see)
print (len(places_to_see))
print (sorted(places_to_see))
print(places_to_see)
places_to_see.sort()
print (places_to_see)
places_to_see.reverse()
print(places_to_see)
places_to_see.reverse()
places_to_see.sort()
print (places_to_see)

# More Sorting Practice
# Permanently sort and revsere sort
b_words = []
b_words.append("butter")
b_words.append("bronco")
b_words.append("buzzer")
b_words.append("bbq")
print (b_words)
b_words.sort()
print (b_words)
b_words.sort(reverse=True)

# Temporarily sort a list
r_words = ['ride','rhino','ribbon','red','rainbow']
print (sorted(r_words))

# Print list in Reverse
r_words.reverse()
print (r_words)


# More List Practice
fruit_list =  ['apples','oranges','pears']
print (fruit_list[-1].upper())
print ("I've always liked " + fruit_list[1].title()
+ " the best!")
fruit_list[1] = 'strawberries'
print("How many " + fruit_list[1] + " can I have?")


animals = ['birds', 'turles','dogs']
print("i love " + animals[1])
animals[1] = 'cats'
print ("I love " + animals[1])
animals.append('cats')
print (animals)

# Add stuff to an Empty List
# Then delete some of the stuff
empty = []
empty.append("Apples")
empty.append("Oranges")
empty.append("Bread")
print (empty)
print (empty[1])
empty[1] = "Milk"
print (empty[1])
empty.append("Eggs")
empty.append("Cheese")
print (empty)
del empty[0]
print (empty)
# Use pop(), show that you can still access popped item
popped = empty.pop()
print (popped)

to_visit = ['sydney','milan','cairo']
to_visit.sort(reverse=True)
print(to_visit)

to_eat = ['berry', 'toast', 'cracker']
print (sorted(to_eat))
to_eat.reverse()
print(to_eat)
print (len(to_eat))

# More Practice
pens = ['ball point','fountain','gel']
print(pens[0].title())
print(pens[1].title())
print(pens[2].title())

for pen in pens:
    print("I love " + pen + " pens")

print (pens[0].title() + " are my favorite")

monsters = []
monsters.append('goblin')
monsters.append('vampire')
monsters.append('devil')
print (monsters)
print (monsters[0].title())
monsters[0] = 'fire ball'
print (monsters)
monsters.insert(0,'grizzly square')
print (monsters)
monsters.insert(1,'charmander')
print (monsters)
del monsters[1]
print (monsters)
monsters.pop(1)
popped_monsters = monsters.pop()
print (popped_monsters)
print (monsters)
monsters.remove('vampire')
print (monsters)

jam = ['raspberry','blueberry','strawberry']
jam[0] = 'apple'
print (jam[-1])
jam.append('current')
print (jam)
jam.insert(1,'banana')
jam.insert(1,'carrot')
print (jam)
del jam[0]
# jam.pop()
# jam.remove('banana')
# jam.sort()
# jam.sort(reverse=True)
print(sorted(jam))
print (jam)
print(len(jam))

yellow_stuff = []
yellow_stuff.append('banana')
yellow_stuff.append('daisy')
yellow_stuff.append('ped Xing sign')
print(yellow_stuff[0].title())
print(yellow_stuff[-1].title())
print("I have 3 " + yellow_stuff[0] + "s in my bag.")
