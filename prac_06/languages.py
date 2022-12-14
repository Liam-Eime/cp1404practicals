"""
CP1404 | Practical 06 - programming_language and languages  | Liam Eime
Estimate: 20 minutes
Actual: 23 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Print languages with dynamic typing"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
