"""
CP1404 | Practical 04 - lists_warmup  | Liam Eime
Program to test some list properties and behaviours
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers, returns true
# 7 in numbers, returns false
# "3" in numbers, returns false
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# print(numbers[0])
# print(numbers[-1])
# print(numbers[3])
# print(numbers[:-1])
# print(numbers[3:4])
# print(5 in numbers)
# print(7 in numbers)
# print("3" in numbers)
# print(numbers + [6, 5, 3])

# change first element of numbers to "ten"
numbers[0] = "ten"

# change last element of numbers to 1
numbers[-1] = 1

# print all elements from numbers except the first two
print(numbers[2:])

# print whether 9 is an element of numbers
print(9 in numbers)
