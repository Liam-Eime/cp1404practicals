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
        print(email_list)
        email = input("Email: ")


main()
