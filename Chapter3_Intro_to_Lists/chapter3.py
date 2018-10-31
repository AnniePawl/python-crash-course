# Lists
# A list is a collection of items in a particular orderself.
# You can put anything in a list
bicycles = ['cannondale', 'trek', 'redline']
print (bicycles)

# Indexing
# Don't forget indexing starts at zero!
# You can access specific parts of list
print (bicycles[0])
print (bicycles[0].title())
# -1 always returns last item in a list
print (bicycles[-1])

message = "My First bicycle was a " + bicycles[0].title() + "!"
print (message)

# To change the value in a list, use name of list followed by index of item you want to change, followed by new replacement value.
motorcycles = ['yamaha','suzuki','honda']
print (motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# To add elements to a list use .append
motorcycles.append('bike')
print (motorcycles)
# To delete elements from a list use del
del motorcycles[0]
print (motorcycles)
# To insert an item into a list use insert()
motorcycles.insert(0, 'ducati')
print (motorcycles)

# Removing items using pop() method
# Will remove an item from any position
popped_motorcycle = motorcycles.pop(2)
print (motorcycles)
print (popped_motorcycle)

# Removing items by value
motorcycles.remove('ducati')

# ORGANIZING Lists
# sort() method to permanently sort
cars = ['honda', 'toyota', 'mazda', 'ford']
cars.sort()
print(cars)
# Reverse Alphabetical Order
cars.sort(reverse=True)
print (cars)
# Temporarily Sorting Lists - Use sorted() function
# This is maintain original order but present it in a sorted order
print(sorted(cars))
# Printing in reverse order
print (cars.reverse())
# Finding the length of a list
print (len(cars)
