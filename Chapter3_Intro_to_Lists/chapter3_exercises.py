# Sort the names of some friends. Print each name by accessing each element one at a time
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
