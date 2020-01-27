# LISTS
Lists are awesome!
- Lets you store info in one place
- A collection of items in a particular order
- You can put anything in a list
- Square brackets [ ] indicate a list
- List items seperated by commas'''

```python
bicycles = ['cannondale', 'trek', 'redline']
print (bicycles)

fruits = ['cherry', 'banana', 'kiwi']
print(fruits)
```

## INDEXING
Indexing allows you to access specific parts of a List
-  Indexing starts at zero! [1] is second item
- To acccess last item, use special syntax [-1]
- Index [-2] returns second to last, etc

```python
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
```

```python 
message = "My first bike was a " + bicycles[-1].title()
print(message)
```

### MODIFY ELEMENTS IN A LIST
**To change a list value**:  <br>
   List name, followed by item index, followed by new value

```python
motorcycles = ['yamamha','honda','suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
```

#### .append 
`.append` to add more items to the list(at end)
```python
motorcycles.append('ducati')
motorcycles.append('blank')
print(motorcycles)
```
#### insert() 
`insert()`to insert item in specific location
- Specify index, follwed by by value
```python 
motorcycle.insert(0, 'ducati')
print(motorcycles)
```

#### del 
del to delete items from a list, just provide index
```python
del motorcycles[0]
del motorcycles[1]
print (motorcycles)
```

#### Removing items by VALUE
In this case, even though ducati was removed from the list, it is still stored in a variable, allowing us to print a statement about it
```python
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("A " + too_expensive.title() + " is too expensive")
```

#### pop() 
Use `pop()` method to remove items, usually last item 
- Can remove an item from any location, too
- Item no longer in list, BUT...
- Helpful b/c lets you work with item after pop!
```python
popped_motorcycle = motorcycles.pop(2)
print (motorcycles)
print (popped_motorcycle)

first_owned = motorcycles.pop(0)
last_owned = motorcycles.pop()
print("The first motorcycle I owned was a " + first_owned + ". The last motocycle I owned was a " + last_owned)
```

#### ORGANIZING Lists
# sort() method 
Use `sort()`  to PERMANENTLY sort (Alphabetically!)
```python
cars = ['honda', 'toyota', 'mazda', 'ford']
cars.sort()
print(cars)
```

#### (reverse = True)
Specify `reverse = True` to return reverse alphabetical order
```python
cars.sort(reverse = True)
print(cars)
# Printing in REVERSE ORDER (NOT alphabetical)
# PERMANENT Change
print (cars.reverse())
```

#### sorted() 
Use `sorted()` to TEMPORARILY sort lists <br>
This maintains original order, but presents sorted order
`print(sorted(cars))`

#### len() method
Use to find legnth of a list
`print (len(cars)`

#### AVOIDING INDEX ERRORS
Be careful of 'list index out of range'
