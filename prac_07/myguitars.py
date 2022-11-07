"""
CP1404 | myguitars | Liam Eime

"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"

guitars = []
with open(FILENAME, 'r') as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

for guitar in guitars:
    print(guitar)
