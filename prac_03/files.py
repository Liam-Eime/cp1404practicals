"""
CP1404 | Practical 03 - files  | Liam Eime
Program to read and write to files
"""
FILE_NAME = "name.txt"

name = input("Enter name: ")
name_text = open(FILE_NAME, 'w')
print(f"{name}", file=name_text)
name_text.close()

name_text = open(FILE_NAME, 'r')
text = name_text.read()
print(f"Your name is {text}")
name_text.close()

numbers_text = open("numbers.txt", 'r')
first_number = int(numbers_text.readline())
second_number = int(numbers_text.readline())
print(f"Total of first two numbers if {first_number + second_number}")
numbers_text.close()
