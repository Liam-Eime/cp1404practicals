"""
CP1404 | Practical 02 - password_stars | Liam Eime
Program to get password with error checking
"""


def main():
    """Get password, checks length and prints stars"""
    minimum_password_length = 5
    password = get_password(minimum_password_length)
    print_asterisks(password)


def get_password(minimum_password_length):
    """Get password and check if it is a valid length"""
    password = input("Enter password: ")
    while len(password) < minimum_password_length:
        print("Password too short, must be at least {} characters".format(minimum_password_length))
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print number of asterisks equal to the length of the password"""
    print('*' * len(password))


main()
