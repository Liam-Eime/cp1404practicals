"""
CP1404 | Practical 01 - sales_bonus | Liam Eime
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# getting sales from user
sales = float(input("Enter sales: $"))

while sales >= 0:
    # conditional logic for bonus
    if sales < 1000:
        # calculating bonus
        bonus = 0.1 * sales
        # printing result
        print("Your bonus is: ${:.2f}".format(bonus))
    else:
        # calculating bonus
        bonus = 0.15 * sales
        # printing result
        print("Your bonus is: ${:.2f}".format(bonus))
    # getting sales from user again
    sales = float(input("Enter sales: $"))
