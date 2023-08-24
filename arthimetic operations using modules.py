import math
#addition
result = math.fsum([1.1, 2.2, 3.3])
print(result)
print("*------------------------------------------------------------------------*")
# Using math.floor() for integer division (floor division)
#Round down to the nearest integer
a = 10
b = 3
result = math.floor(a / b)
print(result)  # Output: 3

# Using math.ceil() for ceiling division
# Round up to the nearest integer
result = math.ceil(a / b)
print(result)  # Output: 4

print("*------------------------------------------------------------------------*")

#substraction
result = a - b
print(result)

print("*------------------------------------------------------------------------*")

#multiplication
#only in python 3.8
numbers = [2, 3, 4, 5]
result = math.prod(numbers)
print(result)
print("*------------------------------------------------------------------------*")

