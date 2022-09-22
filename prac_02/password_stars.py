"""
CP1404 | Practical 01 - menus | Liam Eime
Program to ...
"""

password = input("Enter password: ")
minimum_password_length = 5
while len(password) < minimum_password_length:
    print("Password too short, must be at least {} characters".format(minimum_password_length))
    password = input("Enter password: ")
print('*' * len(password))
