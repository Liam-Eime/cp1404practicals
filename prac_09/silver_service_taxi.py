"""
CP1404 | Liam Eime | Silver service taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver service taxi that inherits from taxi class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver service taxi instance based on a taxi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string like Taxi but with flagfall added to end"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Get fare same as taxi class with the addition of the flagfall cost"""
        return super().get_fare() + self.flagfall
