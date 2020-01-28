## Lists
- List are a collection of items in a particular order
- You can put anything in a list!
- Lists let you store info in one place
- Square brackets `[ ]` indicate a list
- List items are seperated by commas `,`

```python
bicycles = ['cannondale', 'trek', 'redline']
fruits = ['cherry', 'banana', 'kiwi']
```

### Indexing
Indexing allows you to access specific parts of a list. Specify index in brackets `[ ]`
```python
print(bicycles[0]) # returns 1st item, indexing starts at 0
print(bicycles[-1]) # returns last item, special syntax
print("My first bike was a " + bicycles[-2].title()) # returns 2nd to last item
```

### Modify Elements in a List
**Replace list item: ** List name, item index, new value
```python
motorcycles = ['yamamha','honda','suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
```

**.append() Method** <br>
`.append()` to add more items to the list   (at end)
```python
motorcycles.append('ducati')
motorcycles.append('blank')
```

**.insert() Method** <br>
`insert()` to insert item in specific location. Specify index, follwed by by value
```python 
motorcycle.insert(0, 'ducati')
```

**del** <br>
`del` to delete items from a list, just provide index
```python
del motorcycles[0]
del motorcycles[1]
```

**Removing Ttems by Value** <br>
In this case, even though ducati was removed from the list, it is still stored in a variable, allowing us to print a statement about it
```python
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("A " + too_expensive.title() + " is too expensive")
```

**pop() Method** <br>
Can remove an item from any location, but typically used for last item <br>
Item no longer in list, BUT... Helpful b/c lets you **work with item after pop**
```python
popped_motorcycle = motorcycles.pop(2)
print (motorcycles)
print (popped_motorcycle)

first_owned = motorcycles.pop(0)
last_owned = motorcycles.pop()
print("The first motorcycle I owned was a " + first_owned + ". The last motocycle I owned was a " + last_owned)
```

### Organizing Lists
#### Permanent Changes
- **sort() Method** Permanently sorts list in **alphabetical** order
- **sort(reverse = True)** Permenently sorts in **reverse alphabetical** order
- **reverse() Method** PERMANENTLY sorts list in **backwards order** (not alphabetical)
```python
cars = ['honda', 'toyota', 'mazda', 'ford']
cars.sort()
cars.sort(reverse=True)
```

#### Temporary Changes
- **sorted()** to TEMPORARILY sort lists in **alphabetical order** <br>
This maintains original order, but presents/prints sorted order <br>
- **sorted(reverse = True)** will print in REVERSE ALPHABETICAL order

### Length
`len()` method used to find legnth of a list <br>
`print (len(cars)`
