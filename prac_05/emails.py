"""
CP1404 | Practical 05 - emails  | Liam Eime
Program to store users' emails and names in a dictionary
Estimate: 45 minutes
Actual:
"""


def main():
    """Store users emails and names in a dictionary"""
    email = input("Email: ")
    while email != "":
        email_list = email.split("@")
        email_title = email_list[0].split(".")
        try:
            first_name = email_title[0].title()
            last_name = email_title[1].title()
            print(f"{first_name}, {last_name}")
        except IndexError:
            first_name = email_title[0].title()
            print(f"{first_name}")
        email = input("Email: ")


main()
