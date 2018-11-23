# CLASSES
    # Should be capitalized
    # Written in CamelCaps
    # Intance and module names written in lowercase w/ underscres
    # Every class shoud have docstring immediate after def
    # Blank Spaces
        # 1 line btwn methods in a class
        # 2 lines between seperate classes
    # In OOP they represent real-world things and situations
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
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        '''print statement showing car's mileage'''
        print("This car has " + str(self.odometer_reading) + " miles on it")

my_new_car = Car('BMW', 'a7', '1999')
my_new_car.read_odometer()

# MODIFYING ATTRIBUTE VALUES
# You can change in 3 ways:
    # Change value directly through an instance
    # Set value through method
    # Increment the Value through a method

# Modifying Attribue value DIRECTLY
    # This is teh simples way
    # Use dot notation to access value, reset it
my_new_car.odometer_reading = 33
my_new_car.read_odometer()

# Modifying Attribute Value THROUGH METHOD
    # Helpful to have methods that update attributes for you
    # Pass new value to a method that handles updating internally
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        '''print statement showing car's mileage'''
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        '''Set the odometer to given value
        Reject change if attemps to roll back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('BMW', 'a7', '1999')
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# INCREMENTING Attribute Value THROUGH METHOD
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''return nearly formatted descriptive name'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        '''print statement showing car's mileage'''
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        '''Set the odometer to given value
        Reject change if attemps to roll back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''add given amount to odometer reading'''
        self.odometer_reading += miles

my_used_car = Car('subaro','outback','2013')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(1000)
my_used_car.read_odometer()


# INHERIANCE
    # When one class inherits from another, it automatically takes on all attributes and methods of first class
    # Original class called, PARENT CLASS
    # New class called, CHILD CLASS
    # While child class inherits from parent, it can also define new attributes and methods of its own

# INIT METHOD for CHILD CLASS
    # Create a new class that does everything Car class does
    # Name of parent class must be in (parenthesis) in child class definition
# SUPER Function !
    # helps python make connections between parent & child
class Electric_car(Car):
    '''represent aspects of car, specific to electric cars'''

    def __init__(self, make, model, year):
        '''initialize parent class attributes'''
        super().__init__(make, model, year)

my_tesla = Electric_car('tesla','model s','2015')
print(my_tesla.get_descriptive_name())

# DEFINING ATTRIBUTES & METHODS for CHILD CLASS
    # you can add more to differentiate child from parent
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        '''print statement describing battery'''
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

my_tesla = ElectricCar('tesla','model s','2013')
my_tesla.describe_battery()


# OVERRIDING METHODS from the PARENTS CLASS
    # you can override methods that don't fit with what you're trying to model child
    # Define method with same name as in method you want to override  in parent class
    '''def fill_gas_tank():
        '''electric cars dont have gas tanks'''
        print("This car doesn't need gas!")
        '''

# INSTANCES AS ATTRIBUTES
    # Sometimes good to reorganize classes into smaller classes
    class Battery(self):
