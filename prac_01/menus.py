"""
CP1404 | Practical 01 - menus | Liam Eime
Program to create simple menu and handle input within it
"""

# getting name
name = input("Enter name: ")

# setting up menu
MENU = """H - Hello "name"
G - Goodbye "name"
Q - Quit"""
print(MENU)

# getting choice
choice = input(">>> ").upper()

# handling choice
while choice != "Q":
    if choice == "H":
        print("Hello {}".format(name))
    elif choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid message")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")
