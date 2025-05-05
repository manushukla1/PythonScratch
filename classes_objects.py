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


# Inheritance
"""
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    pass  # Inherits everything from Parent

c = Child()
c.greet()  # Output: Hello from Parent!
"""

# If the child has a method with the same name, it overrides the parent’s method.
# super() lets you call the parent’s methods inside the child’s methods.
"""
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child!")

c = Child()
c.greet()
"""
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    pass

my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())   # ?
print(my_cat.speak())   # ?

# types of inheritance -----------------
"""
Single Inheritance --- One child class inherits from one parent class."""  # Used when: You want a class to reuse behavior from just one parent class.
"""Multilevel Inheritance --- Child class inherits from a class that itself is a child of another class. """ #Used when: You want a deeper hierarchy,
# like Animal → Mammal → Dog.
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):  # inherits from Animal
    def walk(self):
        print("Walking")

class Dog(Mammal):  # inherits from Mammal
    def bark(self):
        print("Woof!")

d = Dog()
d.eat()   # from Animal
d.walk()  # from Mammal
d.bark()  # from Dog
""" 
Multiple Inheritance --- A class inherits from more than one parent class.""" # Used when: A class needs features from multiple sources.
class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Flyable, Swimmable):  # inherits from both
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()    # from Flyable
d.swim()   # from Swimmable
d.quack()  # from Duck

# super() --- The super() function gives you access to methods from the parent class without directly naming it. This is especially useful when overriding methods in the child class, like __init__().


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Calls the parent constructor
        self.breed = breed
        print(f"Dog created: {self.name}, Breed: {self.breed}")

d = Dog("Buddy", "Golden Retriever")


# decorators

*