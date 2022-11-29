"""
CP1404 | Liam Eime | Silver service taxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test silver service taxi class"""
    silver_service_taxi = SilverServiceTaxi("Silver service taxi", 100, 2)
    print(f"{silver_service_taxi.name} drove {silver_service_taxi.drive(18)}km"
          f" with a fare of ${silver_service_taxi.get_fare():.2f}")


main()
