"""
CP1404 | Practical 05 - hex_colours  | Liam Eime
Program to look up hexadecimal colour codes
"""

COLOUR_TO_CODE = {"candy apple red": "#ff0800", "amaranth": "#e52b50", "brick red": "#cb4154",
                  "bright maroon": "#c32148", "burgundy": "#800020", "cadmium red": "#e30022",
                  "cardinal": "#c41e3a", "carmine": "#960018", "carnelian": "#b31b1b",
                  "crimson": "#dc143c"}

colour = input("Enter a valid colour: ").lower()
while colour != "":
    try:
        print(f"The code for {colour} is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid colour")
        colour = input("Please enter a valid colour: ").lower()
    colour = input("Enter a valid colour: ")
