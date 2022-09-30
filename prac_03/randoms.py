"""
CP1404 | Practical 03 - randoms | Liam Eime
Program to produce a random number between 1 and 100 inclusive
"""

# line 1 print(random.randint(5, 20))
# smallest possible number is 5

# line 2 print(random.randrange(3, 10, 2))
# smallest possible number is 3
# line 2 could not have produced a 4

# line 3 print(random.uniform(2.5, 5.5))
# smallest possible number is 2.5
# largest possible number is 5.5

import random
print(random.randint(1, 100))
