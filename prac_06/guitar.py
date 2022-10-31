"""
CP1404 | Practical 06 - guitar  | Liam Eime
Estimate: 45 minutes
Actual:
"""

CURRENT_YEAR = 2022


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

    def get_age(self):
        """Return how old the guitar is"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old"""
        if self.get_age() >= 50:
            return True
        else:
            return False
