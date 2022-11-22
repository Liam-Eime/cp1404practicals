"""
CP1404 | Liam Eime | unreliable car class
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Subclass of Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance based on parent car instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive same as parent car but with reliability determining success"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
