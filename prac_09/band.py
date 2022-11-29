"""
CP1404 | Liam Eime | band class
"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Initialise band class instance"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band"""
        return f"{self.name} ({', '.join([musician.__str__() for musician in self.musicians])})"

    def add(self, musician):
        """Add member to band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the bands and the instruments they play"""
        return '\n'.join([musician.play() for musician in self.musicians])
