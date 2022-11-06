"""
CP1404 | Practical 06 - guitar  | Liam Eime
Program to use Guitar class
This program uses a list to store all user's guitars and print their details
Estimate: 30 minutes
Actual: 42 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Use Guitar class to get guitars and their details, and print them"""
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year}) : {cost:,.2f} added.")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")

    # Guitars for testing
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    if guitars:
        max_guitar_name_length = max(len(guitar.name) for guitar in guitars)
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{max_guitar_name_length}} ({guitar.year}), "
                  f"worth $ {guitar.cost:10,.2f}{vintage_string}")
    else:
        print("You have no guitars :P")


main()
