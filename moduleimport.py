import Modules_pacakges
print("Addition: ", Modules_pacakges.add(10, 5))
print("Subtraction: ", Modules_pacakges.subtract(10, 5))
print("Multiplication: ", Modules_pacakges.multiply(10, 5))

try:
    print("Division: ", Modules_pacakges.divide(10, 2))
    print("Division: ", Modules_pacakges.divide(10, 0))  # This will raise an error
except ValueError as e:
    print(e)
