"""
CP1404 | Practical 05 - wimbledon  | Liam Eime
Program to read and process Wimbledon data
Estimate: 60 minutes
Actual:
"""

FILENAME = "wimbledon.csv"
wimbledon_records = []
champion_to_count = {}
countries = set()


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # read first line to remove header
        for line in in_file:
            wimbledon_records.append(line.split(","))

    for record in wimbledon_records:
        countries.add(record[1])
        champion_to_count[record[2]] = champion_to_count.get(record[2], 0) + 1
    print(champion_to_count)


main()
