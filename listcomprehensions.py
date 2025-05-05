#basic syntax -- [expression for item in iterable]

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# with conditions -- [expression for item in iterable if condition]

even_numbers = [x for x in range(10) if x % 2==0]
print(even_numbers)

# multiple conditions

divisible_by_2_and_3 = [x for x in range (20) if x%2 ==0 and x%3 ==0 ]
print(divisible_by_2_and_3)

#Nested List Comprehension --List comprehensions can also be nested to handle multi-dimensional
# data structures like lists of lists. Syntax -- [[expression for item in sublist] for sublist in iterable]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat =[]
for row in matrix:
    for num in row:
        flat.append(num)

print (flat)   # here I have flattened it using the simple loops


Multiplying_Elements_from_Two_Lists  = [x * y for x in [1,2,3] for y in [10,100]]
print (Multiplying_Elements_from_Two_Lists)
result =[]
for x in [1,2,3]:
    for y in [10,100]:
        result.append(x*y)
print(result)

# Challenge: Flatten and Filter Even Numbers
matrix = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
]

even_numbers = [num for row in matrix for num in row if num % 2==0]
print(even_numbers)