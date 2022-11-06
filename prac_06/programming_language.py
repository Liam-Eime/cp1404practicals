"""
CP1404 | Practical 06 - programming_language and languages  | Liam Eime
Estimate: 20 minutes
Actual: 23 minutes
"""


class ProgrammingLanguage:
    """Represent programming language information"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return programming language information"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if the typing is dynamic"""
        return self.typing == "Dynamic"
