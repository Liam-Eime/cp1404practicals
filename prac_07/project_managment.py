"""
CP1404 | project and project management | Liam Eime
Estimate time = 1.5hrs
Actual time =
"""

import datetime
from prac_07.project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Handle projects"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects_from_file(filename)
            for project in projects:
                print(project)
        elif choice == "S":
            print("S")
        elif choice == "D":
            print("D")
        elif choice == "F":
            print("F")
        elif choice == "A":
            print("A")
        elif choice == "U":
            print("U")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects_from_file(filename):
    """Load projects from filename"""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # 'absorb' header
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


if __name__ == '__main__':
    main()
