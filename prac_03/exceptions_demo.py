"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
while denominator != 0:
    try:
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")
print("Cannot divide by zero!")

# ValueError will occur when either numerator and/or denominator are not numbers
# ZeroDivisionError will occur when the denominator is zero and numerator is a valid number
