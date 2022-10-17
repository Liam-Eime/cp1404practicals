"""
CP1404 | Practical 04 - list_comprehensions  | Liam Eime
Program to look up hexadecimal colour codes
"""

COLOUR_TO_CODE = {"Candy Apple Red": "#ff0800", "Amaranth": "#e52b50", "Brick Red": "#cb4154",
                  "Bright Maroon": "#c32148", "Burgundy": "#800020", "Cadmium Red": "#e30022",
                  "Cardinal": "#c41e3a", "Carmine": "#960018", "Carnelian": "#b31b1b",
                  "Crimson": "#dc143c"}

colour = input("Enter a valid colour: ")
while colour != "":
    try:
        print(f"The code for {colour} is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid colour")
        colour = input("Please enter a valid colour: ")
    colour = input("Enter a valid colour: ")
