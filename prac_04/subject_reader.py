"""
CP1404 | Practical 04 - subject_reader  | Liam Eime
Program to convert data file into lists
"""

FILENAME = "subject_data.txt"


def main():
    """get data as a list of lists and display the subject details"""
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students, and return as list of lists."""
    input_file = open(FILENAME)
    data_lists = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_lists.append(parts)
    input_file.close()
    return data_lists


def display_subject_details(data):
    """Display the subject details in an easy-to-read manner"""
    for part in data:
        print(f"{part[0]} is taught by {part[1]} and has {part[2]} students")


main()
