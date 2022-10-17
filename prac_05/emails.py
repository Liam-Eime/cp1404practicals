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
        name = extract_name_from_email(email)
        print(name)
        email = input("Email: ")


def extract_name_from_email(email):
    email_list = email.split("@")
    email_title = email_list[0].split(".")
    try:
        first_name = email_title[0].title()
        last_name = email_title[1].title()
        names = [first_name, last_name]
        name = " ".join(name for name in names)
        return name
    except IndexError:
        name = email_title[0].title()
        return name


main()
