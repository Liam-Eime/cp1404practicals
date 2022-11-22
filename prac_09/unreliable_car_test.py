"""
CP1404 | Liam Eime | unreliable car test
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test unreliable car class"""
    car1 = UnreliableCar("Always reliable car", 200, 100)
    car2 = UnreliableCar("Mostly reliable car", 200, 75)
    car3 = UnreliableCar("Half reliable car", 200, 50)
    car4 = UnreliableCar("Mostly unreliable car", 200, 25)
    car5 = UnreliableCar("Always unreliable car", 200, 0)

    for i in range(5):  # attempt to drive all five cars by 20km, 5 times, to test reliability
        print(f"TEST {i+1}\n")
        print(f"{car1.name} drove {car1.drive(20)}km")
        print(f"{car1}\n")
        print(f"{car2.name} drove {car2.drive(20)}km")
        print(f"{car2}\n")
        print(f"{car3.name} drove {car3.drive(20)}km")
        print(f"{car3}\n")
        print(f"{car4.name} drove {car4.drive(20)}km")
        print(f"{car4}\n")
        print(f"{car5.name} drove {car5.drive(20)}km")
        print(f"{car5}\n")


main()
