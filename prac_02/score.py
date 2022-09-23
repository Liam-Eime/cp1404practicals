"""
CP1404 | Practical 02 - score | Liam Eime
Program to rate inputted and random scores
"""
import random


def main():
    """Rate both inputted and random score"""
    score = float(input("Enter score: "))
    print(rate_score(score))

    random_score = random.randint(0, 100)
    print("Random score: {}".format(random_score))
    print(rate_score(random_score))


def rate_score(score):
    """Rate inputted score to return its rank"""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
