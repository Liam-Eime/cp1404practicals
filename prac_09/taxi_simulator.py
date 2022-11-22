"""
CP1404 | Liam Eime | Taxi simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Taxi simulator program"""
    total_trip_cost = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
        elif choice == "d":
            print("d")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def display_taxis(taxis):
    """Display taxis available"""
    pass


main()
