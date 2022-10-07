"""
CP1404 | Practical 04 - quick_picks | Liam Eime
Program to ...
"""
import random

LENGTH_OF_QUICK_PICK = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(LENGTH_OF_QUICK_PICK):
        random_number = random.randint(MINIMUM, MAXIMUM)
        while random_number in quick_pick:
            random_number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(random_number)
        quick_pick.sort()
    print(quick_pick)
