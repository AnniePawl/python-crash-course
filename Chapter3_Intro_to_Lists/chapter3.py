# LISTS
'''Lists are awesome!
   - Lets you store info in one place
   - A collection of items in a particular order
   - You can put anything in a list
   - Square brackets [ ] indicate a list
   - List items seperated by commas'''

bicycles = ['cannondale', 'trek', 'redline']
print (bicycles)

fruits = ['cherry', 'banana', 'kiwi']
print(fruits)


# INDEXING
''' - Indexing allows you to access specific parts of a List
    - Indexing starts at zero! [1] is second item
    - To acccess last item, use special syntax [-1]
    - Index [-2] returns second to last, etc'''

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = "My first bike was a " + bicycles[-1].title()
print(message)


# MODIFY ELEMENTS IN A LIST
'''To change a list value:
   List name, followed by item index, followed by new value'''

motorcycles = ['yamamha','honda','suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

# .append to add more items to the list(at end)
motorcycles.append('ducati')
motorcycles.append('blank')
print(motorcycles)

# insert() to insert item in specific location
# Specify index, follwed by by value
motorcycle.insert(0, 'ducati')
print(motorcycles)

# del to delete items from a list, just provide index
del motorcycles[0]
del motorcycles[1]
print (motorcycles)

# Removing items by VALUE
'''In this case, even though ducati was removed from the list, it is still stored in a variable, allowing us to print a statement about it.'''
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("A " + too_expensive.title() + " is too expensive")

# pop() method to remove items
''' - pop() is usually used to remove last item
    - Can remove an item from any location, too
    - Item no longer in list, BUT...
    - Helpful b/c lets you work with item after pop!'''
popped_motorcycle = motorcycles.pop(2)
print (motorcycles)
print (popped_motorcycle)

first_owned = motorcycles.pop(0)
last_owned = motorcycles.pop()
print("The first motorcycle I owned was a " + first_owned + ". The last motocycle I owned was a " + last_owned)

# ORGANIZING Lists
# sort() method to PERMANENTLY sort (Alphabetically!)
cars = ['honda', 'toyota', 'mazda', 'ford']
cars.sort()
print(cars)
# REVERSE ALPHABETICAL Order
# (reverse = True)
cars.sort(reverse = True)
print(cars)
# Printing in REVERSE ORDER (NOT alphabetical)
# PERMANENT Change
print (cars.reverse())

# TEMPORARILY Sorting Lists
# Use sorted() function
# This maintains original order, but presents sorted order
print(sorted(cars))

# Find LENGTH of LIST with len() function
print (len(cars)

# AVOIDING INDEX ERRORS
# Be careful of 'list index out of range'
