"""
CP1404 | Liam Eime | Silver service taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver service taxi that inherits from taxi class"""

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver service taxi instance based on a taxi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
