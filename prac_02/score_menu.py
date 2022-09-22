"""
CP1404 | Practical 02 - score_menu | Liam Eime
Program to get and print a valid score with stars
"""


def main():
    """Main function"""
    score = int(input("Enter Score: "))
    while score > 100 or score < 0:
        print("Invalid score, must be from 0-100")
        score = int(input("Enter Score: "))

    menu = """P - Print score
S - Print stars
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "P":
            print(rate_score(score))
        else:
            print_stars(score)
        print(menu)
        choice = input(">>> ").upper()


def rate_score(score):
    """Rate the inputted score to return its rank"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print a number of asterisks equal to the score"""
    print('*' * score)


main()
