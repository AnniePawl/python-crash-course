    # Like a blueprint or set of instructions

# OBJECTS
    # are created based on classes
    # each is automatically equipped w/ general behavior
    # You can give each whatever unique traits you want

# INSTANTIATION
    # When you make an object from a class

# CREATING & USING A CLASS
    # Dog class w/ traits common to most dogs
class Dog():
    '''simple dog model'''

    def __init__ (self, name, age):
        '''initialize name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''simulate dog stting in response to a command'''
        print(self.name.title() + " is finally sitting.")

    def roll_over(self):
        '''simulate rolling in response to a command'''
        print(self.name.title() + " rolled over!")

# THE __init__() METHOD
    # Methods are functions that are part of aclass
    # Init method is special. Python automatically runs it whenever it creates a new instance
        # SELF PARAMETER
        # Required in method definition
        # Must come before other parameters
        # Every method call associated with a class automatically passes self, which is a reference to instance, itself
        # Gives individual instance access to attributes and methods in the class
        # Every variable has prefix 'self'
        # 'self.blank' is available to every method in the class
        # We can also access these variables through any instance created from the class.
# MAKING AN INSTANCE FROM A CLASS
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# ACCESSING ATTRIBUTES
    # Use dot notation to access instance ATTRIBUTES
my_dog.name
my_dog.age

# CALLING METHODS
    # Use dot notation to call any method defined in class
my_dog.sit()
my_dog.roll_over()

# CREATING MULTIPLE INSTANCES
    # You can create as many instances as you need
my_dog = Dog('carly', 13)
print("My dog's name is " + my_dog.name.title() + ".")
print(my_dog.name.title() + " is now " + str(my_dog.age) + " years old!")


# WORKING WITH CLASSES & INSTANCES
    # You can modify attributes of an instance directly of write methods that update attributes in specific ways
class Car():
    '''simple attempt to represent a car'''
    def __init__(self, make, model, year):
        '''initialize car attributes'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''return nearly formatted descriptive name'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())

# Setting DEFAULT VALUE for ATTRIBUTE
    # Every attribute in a class needs an initial vaue

class Car():
