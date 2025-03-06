#Working with a list
from collections.abc import tuple_iterator

#looping through a list
jadugars = ['rick','martin','suresh','kamlesh']
for jadugar in jadugars: # here we implemented a for loop and taken a variable in which we assign the values from the list. jadugar is the variable name
    print(jadugar)  # python hassociates the current value of magicians
    print (f"{jadugar.title()}, wow good one!") # just played with print function and tweaked the result we can print a message multiple times with a loop

#what if we want to print our result into next lines after every loop ? let's see
    print(f"I can't wait for next trick , {jadugar.title()}\n")  #------- see we used \n for new line , the print leaves a blank line although but we are printing to prints together

# let's come out of loop and print generic line
print("great show")


pizzas = ['capsicum', 'onion', 'corn']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza.title()} pizza\n".title())

print("pizza is lobe\n")

#let's suppose we want to write numbers from 1 to 100 --- use Range() function
for value in range(1, 5):# tis will only print till 1 to 4 this is off-by-one behaviour , python stops at second value like it stops at 5 so we never get 5 to get 5 we go till 6
    print(value)

for values in range(6): #here the values gets printed from 0 to 6 we have not given the initial number so it starts from 0 always
    print(values)

numbers = list (range(1,4)) # use this to make list of numbers directly from range of numbers , sometimes you need a large list just use this
print(numbers)
#how about skipping a numbers ?
num = list(range(3, 30 , 3))  # here 3 is start 30 is end but last 3 means skips 3 values then pint the next one----important
print(num)

empty_list = [] # let's see if we want to add square of a number in list we use an empty list first
for value in  range(1,27): # we use range because we want square values of number between these ranges
    square = value**2 # just taken a variable square whose value we will append into the list
    empty_list.append(value**2) #here we just take teh empty list and append the value of variables or if we don't want to use variable we can do it like this
print(empty_list) # printing
print(min(empty_list)) # method for finding minimum from alist
print(max(empty_list)) # method for finding max from alist
print(sum(empty_list))  # method for finding sum from alist

# list comprehensions - neatly making list
empty_box = [value**2 for value in range(2,8)] # no rocket science just written everything | logic in one line | yahi toh hai logic meri jaaan !!!!!
print(empty_box)


#slicing ---- cheeeer dengey | kaat dengeeey  --- sometimes you want to work with specific elements from the list
players = ['ravi','shastri', 'vibgyor','sheetal']
print(players[0:2]) # we pass the indexes, and we get the values of index 0 and 1 cause at 2 it stops similar to range() method.
print(players[1:4])
print(players[:4]) # first index omit python starts from 0 then
print(players[2:]) # from index two till last all values
for player in players[:3]: #loop through a sliced list we have to initiate the slicing in the looooop
    print(player.title())

foods = ['pizza','rools','springrolls','burger']
friend_food = foods[0:1]
print(friend_food)
friend_food.append('granolla')
print(friend_food )


#tuples-----------------------------------------------------------------! tuples are the list which can never be changed () means tuples |  [] - list
# -- tuples are a simple ds use them when you want to store values when ou know your values never changed
#tuples - suppose you want a mountain in a game whose coordinates or size will always be fixed so we use tuples
size = (400, 50)
print(size[0])
print(size[1])
#size[0]= 40 # this can't be done as tuples can't be changed heehaw
print(size)
new_size = (300,60)
print(size[0])
print(size[1])
print(new_size)











