"""
CP1404 | Practical 01 - shop_calculator | Liam Eime
Program to calculate total price of n items
"""

# setting total to zero initially
total_price_of_items = 0

# user input
number_of_items = int(input("Number of items: "))

# error checking
while number_of_items < 0:
    print("Invalid number of items, please enter a valid number!")
    number_of_items = int(input("Number of items: "))

# getting prices for items and accumulating total
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price_of_items = total_price_of_items + price_of_item

# calculating discount if applicable
if total_price_of_items > 100:
    total_price_of_items = 0.9 * total_price_of_items  # discount of 10% if greater than $100

# printing total
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price_of_items))
