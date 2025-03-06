# if statements
from zoneinfo import available_timezones

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars : #first checks if the current value of car is 'bmw' u.If it is, the value is printed in uppercase. If the value of car is anything other than 'bmw', it’s printed in title case:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())
        print(car.title())


#Conditional Tests #At the heart of every if statement is an expression that can be evaluated as
#True or False and is called a conditional test.
#equality operator a double equal sign (==)

#we can check for equality even when the character case is different by converting it by adding car.lower() == comparison
#check for inequality
requested_topping = 'mushroom'
if requested_topping != 'chikoo': # if this is true run it, if this matches hold on
    print("hold on")
#if we want to check multiple conditions use and | or
#checking if the value is in the list
requested_topping = ['a','b','c','d']
topping = ('e')
if topping in requested_topping:   #we use keyword in and not in to check if the value is present
    print(f"{topping.title()} is  present")
else:
    print(f"{topping.upper()} is not  present")

#Boolean Expressions -- Boolean value is either True or False

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

'''
Simple if Statements
The simplest kind of if statement has one test and one action:
if conditional_test:
       do something
'''
age = 16 # no result as age get <18 and loop never runs
if age >= 18:
    print("You are old enough to vote!")
    print("\nHave you registered to vote yet?") # telling the user to check if they have voter id or not , you can add whatever statement if the condition gets met

#if-else Statements
age = 17
if age >= 18:
   print("You are old enough to vote!")
   print("Have you registered to vote yet?")
else: # this gets run we are lopping an if else condition
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#The if-elif-else Chain -- this is important we use this on daily basis
'''Admission for anyone under age 4 is free.
• Admission for anyone between the ages of 4 and 18 is $25.
• Admission for anyone age 18 or older is $40.'''

age = 12
if age < 4:
   print("Your admission cost is $0.")
elif age < 18:
   print("Your admission cost is $25.")
else:
   print("Your admission cost is $40.")

age = 12
if age < 4:
   price = 0
elif age < 18:
   price = 30
else:
   price = 50
print(f"\nyour admission price is INR {price}")

#Using Multiple elif Blocks

age = 12
if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
   price = 40
else:
  price = 20
print(f"Your admission cost is ${price}.")

#without else block
age = 70
if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
   price = 40
elif age > 65:
  price = 20
print(f"Your admission cost is ${price} cause you are senior.")

#testing multiple conditions --- if there is one test that needs to get passed we use elif blocks but we have multiple conditions we use if blocks again and again
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
   print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
   print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
   print("Adding extra cheese.")
print("\nFinished making your pizza!")
#let's see if we have used elif statement
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
   print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings: #only if gets passed cause beyond that no condition gets triggered cause python doesn't go beyond first case in an if-elif-else chain.
   print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
   print("Adding extra cheese.")
print("\nFinished making your pizza!")

''' if you want only one block of code to run, use an if-elif-
else chain. If more than one block of code needs to run, use a series of
independent if statements.'''
#with list
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping.title()}")
print("pizza ready.".title())

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"sorry we ran out of green peppers".title())
    else:
        print(f"Adding {requested_topping.title()}")
print("pizza ready.".title())

colour = ['green','red','yellow']
for alien_colour in colour:
    if alien_colour == 'green':
        print("earned 5 points".title())
    elif alien_colour != 'green':
        print("earned 10 points".title())

# Checking that list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using multiple list
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding your {requested_topping}".title())
    else:
        print(f"we are not having {requested_topping}".title())
print("pizza ready!")