"""
CP1404 | Practical 03 - password_checker | Liam Eime
Program to ...
"""

MIN_LENGTH = 4
MAX_LENGTH = 20
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower = count_lower + 1
        pass

        if char.isupper():
            count_upper = count_upper + 1
        pass

        if char.isdigit():
            count_digit = count_digit + 1
        pass

        if char in SPECIAL_CHARACTERS:
            count_special = count_special + 1
        pass

    if count_lower == 0:
        return False
    elif count_upper == 0:
        return False
    elif count_digit == 0:
        return False
    else:
        pass

    if count_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
