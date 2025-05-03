'''def positive_number(number):
    if number < 0:
        raise ValueError("Number is not positive")
    else:
        print("Number is positive")

try:
    num = int(input("Enter a number: "))
    positive_number(num)
except ValueError as e:
    print("Error caught:", e)'''


x = int(input("Enter a number: "))
assert x % 2 == 0, "Number must be even!"
print("Great! Number is even.")
