"""
CP1404 | Practical 05 - wimbledon  | Liam Eime
Program to read and process Wimbledon data
Estimate: 60 minutes
Actual:
"""

FILENAME = "wimbledon.csv"
wimbledon_champions = []
champion_to_count = {}


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # read first line to remove header
        for line in in_file:
            wimbledon_champions.append(line.split(","))


main()
