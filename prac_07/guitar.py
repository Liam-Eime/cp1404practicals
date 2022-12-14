"""
CP1404 | Practical 07 - guitar  | Liam Eime
"""

CURRENT_YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    """Represent guitar information"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar information"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Sort by year"""
        return self.year < other.year

    def get_age(self):
        """Return how old the guitar is"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old"""
        return self.get_age() >= VINTAGE_YEAR
