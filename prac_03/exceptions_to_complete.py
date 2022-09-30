"""
CP1404 | Practical 03 - exceptions_to_complete  | Liam Eime
Program to get integer from user and not crash when invalid input
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)  # safe to "may be undefined" for result
