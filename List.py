cycle = ['trek', 'hero ' , 'decath' , 'firefox']
print(cycle) #now here whole list gets printed with square brackets but what if i want to print only the single values or whole list without bracket let's see below
#List is represented in [] square brackets only
print(cycle[0]) # see a single value gets returned without brackets cause i am returning the index value.
print(cycle[0].title(),cycle[1].upper()) #nothing just changing the sentence case using title() and lower() methods.
#index position always starts from 0 not 1 its always n-1 traversing
print(cycle[-1]) #this returns the value from end of the list if you say you want to get values from last of the the list just user - before index value
print(cycle[-3]) #third last item yo
message = f"my first cycle was a {cycle[0]}".title() # see here i have written title after "" so it will make my message into tile format all in all cooooool
print(message)


My_friends = ['Manu', 'Atul', 'Sona'] #part of exercise
print(f"Hi {My_friends[0]} how are you ?")
print(f"Hi {My_friends[1]} how are you ?")
print(f"Hi {My_friends[2]} how are you ?")

#let change the value of one index in a list yeah do it , first element  only
cycle[0] = 'CARRERA'
print(cycle)
print(cycle[0].title(),cycle[1].title(),cycle[2].title(),cycle[3].title(),) #value at index one got modified


# we can modify any value from teh list to a new one but what about adding new value every time for example : subway surfer adding trains and hurdles again and again : let's do it
cycle.append('ktm bikes')
print(cycle) # new value got added into the list at index 5
#but you always start a fresh game so your list will always be empty right ?

Motorbikes = []
Motorbikes.append('honda')
Motorbikes.append('tvs')
Motorbikes.append('bajaj')
print(Motorbikes) # Now our empty list got 3 new entries and these entries are always done in a sequence not in random way like starting from 0,1 and it goes on

# now lets insert a new value at any value
Motorbikes.insert(2, 'h2')
print(Motorbikes)

#now lets remove/delete an element/value from a list
del Motorbikes[0] # at index 0 the value will be deleted honda gets deleted!
print(Motorbikes)
# in the above case the value is permanently deleted and can never be reused again --- but what if we ever encounter a scenario where we need the deleted value in future --
# for that we use pop() method like showing an animation of getting killed in the game so for that we need the location , like maintaining a list of active and inactive users
popped_Motorbikes = Motorbikes.pop() # popped_Motorbikes will hold the value of removed value.
print(Motorbikes) #--- the pop() method always removes the item from last of the list, BAJAJ gets removed.
print(Motorbikes.pop()) # we can implement like this as well without passing the variable value in print function.
print(popped_Motorbikes) # returns the value of deleted value


Bikes = ['Ducati','Kawasaki','Harley','KTM','Yamaha',]
My_Last_Owned = Bikes.pop()
print(f"My Last Owned bike was {My_Last_Owned.title()}")

# Don't worry you can pop any value from any index let's do it.

My_2Last_Owned = Bikes.pop(0) # the first value gets popped from the list.
print(F"My Last Owned bike was {My_2Last_Owned.title()}")
#removing item/element by passing value name let's see
Bikes.remove('Harley') #---------------remove() method
print(Bikes)
print(My_Last_Owned)
print(My_2Last_Owned)

Bike = ['TVS','HONDA','HERO','BULLET','CONTINENTAL','GT']
print(Bike)

too_expensive = 'TVS'
Bike.remove(too_expensive) #passing the reference of a value that is being removed. | if the same value occurs twice only the value first value gets removed to remove all the occurrence we need --
#use a loop
print(Bike)
print (f"\nA {too_expensive.title()} is too expensive for me.")

# a list is never sorted but how about sorting it let's see
Bike.sort() #sort() method is used
print(Bike) # list gets sort alphabetically
# we can sort the list is reverse alphabetical order
Bike.sort(reverse=True) #the T for true remains caps!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(Bike)


# sort() method sorts the list permanently but what if we want to sort the data temporarily we USE SORTED() function
two_wheelers = ['TVS','HONDA','HERO','BULLET','CONTINENTAL','GT']
print(two_wheelers)
print("\n sorted list:")
print(sorted(two_wheelers)) #here the values are returned in sorted order
print(two_wheelers) #original list appears

print(len(two_wheelers)) #len function returns the length of list.














