"""
CP1404 | Practical 01 - broken_score | Liam Eime
Program to rate inputted score
"""

# getting user input
score = float(input("Enter score: "))

# conditional logic for ranking score
if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
