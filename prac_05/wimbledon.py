"""
CP1404 | Practical 05 - wimbledon  | Liam Eime
Program to read and process Wimbledon data
Estimate: 60 minutes
Actual: 58 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Process Wimbledon records and display champions and winning countries"""
    wimbledon_records = get_wimbledon_records(FILENAME)
    countries, champion_to_count = process_wimbledon_records(wimbledon_records)
    display_wimbledon_records(champion_to_count, countries)


def get_wimbledon_records(filename):
    """Get Wimbledon records from file and save as a list of lists"""
    wimbledon_records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # read first line to remove header
        for line in in_file:
            wimbledon_records.append(line.split(","))
    return wimbledon_records


def process_wimbledon_records(wimbledon_records):
    """Process Wimbledon records to get champions, how many times they've won, and what countries have won"""
    champion_to_count = {}
    countries = set()
    for record in wimbledon_records:
        countries.add(record[COUNTRY_INDEX])
        champion_to_count[record[CHAMPION_INDEX]] = champion_to_count.get(record[CHAMPION_INDEX], 0) + 1
    return countries, champion_to_count


def display_wimbledon_records(champion_to_count, countries):
    """Display the champion, their winning tally, and the countries that have won"""
    print("Wimbledon Champions: ")
    for champion in champion_to_count:
        print(f"{champion} {champion_to_count[champion]}")
    print(f"\nThese {len(countries)} have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
