"""
CP1404 | myguitars | Liam Eime
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """"""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")

    guitars.sort()
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(guitar)
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == '__main__':
    main()
