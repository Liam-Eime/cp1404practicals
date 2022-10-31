"""
CP1404 | Practical 06 - guitar  | Liam Eime
Program to test guitar.py Guitar class
(Timing for this file and the guitar.py file was for the completion of both these files)
"""

from guitar import Guitar

CURRENT_YEAR = 2022


def run_tests():
    """Test the Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.4

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2000, 420)

    print(f"{guitar.name} get_age() - Expected {CURRENT_YEAR - year}. Got {CURRENT_YEAR - guitar.year}")
    print(f"{another_guitar.name} get_age() - Expected {CURRENT_YEAR - 2000}. Got {CURRENT_YEAR - another_guitar.year}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()
