#dictionary -- collection of key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['key'] = 'value'
print(alien_0) #this prints the dictionary

alien_1 = {}   #empty dictionary
alien_1['key']  = 'yoyo'
alien_1['value'] ='pair'
print(alien_1)

alien_1['key'] = 'jiji' #we are modifying one value
print(alien_1)


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
              x_increment = 1
elif alien_0['speed'] == 'medium':
              x_increment = 2
else:
# This must be a fast alien.
               x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']  #del deletes the key value pair  --- once the key is removed it is deleted permanently
print(alien_0)

favorite_languages = {    # a dict... of similar object
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
language = favorite_languages['jen'].title()
print(f"\nJen's favourite language is {language}".title())

'''### Note ----- The get() method requires a key as a first argument. As a second
optional argument, you can pass the value to be returned if the key doesn’t
exist'''
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.') # as No key for point is available so we check if there is available we return else we don't 
print(point_value)

print("raviji")