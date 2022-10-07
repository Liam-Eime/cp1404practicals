"""
CP1404 | Practical 04 - quick_picks | Liam Eime
Program to ...
"""
import random

LENGTH_OF_QUICK_PICK = 6

number_of_quick_picks = int(input("How many quick picks? "))
quick_pick = []

for i in range(LENGTH_OF_QUICK_PICK):
    RANDOM_NUMBER = random.randint(1, 45)
    quick_pick.append(RANDOM_NUMBER)

for j in range(number_of_quick_picks):
    print(quick_pick)
