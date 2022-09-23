"""
CP1404 | Practical 02 - score_menu | Liam Eime
Program to get a valid score, with menu options to select to print score or print stars
"""


def main():
    """Get valid score, rate score and print stars"""
    score = get_valid_score()
    menu = """P - Print score
S - Print stars
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "P":
            print(rate_score(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>> ").upper()


def get_valid_score():
    """Get score and check if valid"""
    score = int(input("Enter Score: "))
    while score > 100 or score < 0:
        print("Invalid score, must be from 0-100")
        score = int(input("Enter Score: "))
    return score


def rate_score(score):
    """Rate score to return its rank"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print number of asterisks equal to the score"""
    print('*' * score)


main()
