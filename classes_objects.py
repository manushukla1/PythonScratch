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
