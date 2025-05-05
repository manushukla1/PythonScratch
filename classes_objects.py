# Classes and Objects
"""
class Person:  # Class definition
    pass       # Placeholder for now

# Creating objects (instances) of the class
p1 = Person()
p2 = Person()
"""
# Adding Attributes with __init__()
class person:
    def __init__(self, name , age ):
        self.name = name
        self.age = age

p1 = person ("alice" , 28) # created the object
print(p1.name)
print(p1.age)

# challenge

"""
Can you define a class named Car that:

Takes brand, model, and year as input during object creation.

Stores them as instance variables.

Then, print out the brand and year of the car.
"""
class Car:
    def __init__(self, brand, model , year):
        self.brand = brand
        self.model = model
        self.year = year

my_car = Car("Toyota", "corolla", 2020)
print(my_car.brand)

#instance methods An instance method is a function inside a class that works
# with the data (attributes) of an object (an instance).

class Car:
    def __init__(self, brand, model , year):
        self.brand = brand
        self.model = model
        self.year = year

    # custom instance method
    def description(self):
        return f"{self.year} {self.brand} {self.model}"
    def ageofcar(self):
        if self.year < 2015:
            return "Old car"
        else:
            return  "new car"
my_car = Car("Toyota", "corolla", 2020)
print(my_car.description())
print(my_car.ageofcar())

# what is self in python
"""
In Python, self refers to the current object (instance) of a class.

It is used to:

Access instance variables (like self.brand, self.year)

Call other methods in the same class (self.some_method())

Think of self like “this particular car”. If you had many car objects, self helps Python know which specific one you're talking about.
"""

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        return f"This car is a {self.brand}, made in {self.year}"

car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2014)

print(car1.show_info()) # Uses car1's brand and year
print(car2.show_info()) # Uses car2's brand and year

# Instance Variables vs Class Variables
class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable --- cause it's inside a function __init__

dog1 = Dog("Rex")
dog2 = Dog("Buddy")

print(dog1.name)  # Rex
print(dog2.name)  # Buddy

# Class Variables

class Dog:
    species = "Canine"  # Class variable -- cause it's declared inside a class

    def __init__(self, name):
        self.name = name

dog1 = Dog("Rex")
dog2 = Dog("Buddy")

print(dog1.species)  # Canine
print(dog2.species)  # Canine


