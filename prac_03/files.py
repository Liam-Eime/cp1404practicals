"""
CP1404 | Practical 03 - files  | Liam Eime
Program to read and write to files
"""
FILE_NAME = "name.txt"

with open(FILE_NAME, "w") as name_text:
    name = input("Enter name: ")
    print(f"{name}", file=name_text)

with open(FILE_NAME, "r") as name_text:
    text = name_text.read()
    print(f"Your name is {text}")

with open("numbers.txt", "r") as numbers_text:
    first_number = int(numbers_text.readline())
    second_number = int(numbers_text.readline())
    print(f"Total of first two numbers is {first_number + second_number}")

with open("numbers.txt", "r") as numbers_text:
    total = 0
    for line in numbers_text:
        number_in_line = int(line)
        total = total + number_in_line
    print(total)
