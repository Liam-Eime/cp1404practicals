"""
CP1404 | Practical 03 - files  | Liam Eime
Program to read and write to files
"""
FILE_NAME = "name.txt"

name = input("Enter name: ")
name_text = open(FILE_NAME, 'w')
print("{}".format(name), file=name_text)
name_text.close()

name_text = open(FILE_NAME, 'r')
text = name_text.read()
print(f"Your name is {text}")
name_text.close()
