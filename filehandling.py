from pathlib import Path

'''
file = open("/Users/manushukla/Downloads/pi_digits.txt", "r")
lines = file.readlines()  # ✅ Now this works

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)'''
"""
path = Path('/Users/manushukla/Downloads/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input ("Enter your birthday, in the form of ddmmyy : ")
if birthday in pi_string:
    print ("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
"""

file = open("/Users/manushukla/Downloads/pi_digits.txt", "w",)
file.write("Manu,\n")
file.write("Shukla\n")
file.close()
file = open("/Users/manushukla/Downloads/pi_digits.txt", "r")
print(file.read())

# ➕ If you want to add to the file (instead of overwriting), use 'a':
file = open("/Users/manushukla/Downloads/pi_digits.txt", "a",)
file.write("don")
file = open("/Users/manushukla/Downloads/pi_digits.txt", "r")
print(file.read())

# Best Practice: Use with (auto closes file)
#  .writelines() – What Is It?
lines = ["Manu shukla,\n"
         "pyhton coder"]

file = open("/Users/manushukla/Downloads/pi_digits.txt", "r+",)
file.writelines(lines)
file = open("/Users/manushukla/Downloads/pi_digits.txt", "r")
print(file.read())


