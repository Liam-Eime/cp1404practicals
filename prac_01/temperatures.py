"""
CP1404 | Practical 01 - temperature | Liam Eime
Program to convert between Celsius and Fahrenheit
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # getting user input
        fahrenheit = float(input("Fahrenheit: "))
        # conversion
        celsius = 5 / 9 * (fahrenheit - 32)
        # displaying the result
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")