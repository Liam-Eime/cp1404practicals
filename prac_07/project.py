"""
CP1404 | project and project management | Liam Eime
Estimate time = 1.5hrs
Actual time = 2hrs 45min
"""


class Project:
    """Represent project information"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise variables"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return project information"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Define "<" for sorting by priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Check if project is complete"""
        return self.completion_percentage == 100
