"""
CP1404 | Practical 05 - emails  | Liam Eime
Program to store users' emails and names in a dictionary
Estimate: 45 minutes
Actual: 59 minutes
"""


def main():
    """Store users emails and names in a dictionary"""
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = extract_name_from_email(email)
        email_to_name[email] = name
        is_name_correct = input(f"is your name {email_to_name[email]} correct? (Y/N)")
        if is_name_correct.upper() != 'Y' and is_name_correct.upper() != '':
            name = input("Name: ")
            email_to_name[email] = name
        email = input("Email: ")

    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")


def extract_name_from_email(email):
    """Extract name from email and return name"""
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
