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
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects_from_file(filename)
        elif choice == "S":
            filename = input("Enter filename: ")
            save_projects_to_file(filename, projects)
        elif choice == "D":
            projects.sort()
            display_projects(projects)
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
    """Load projects from file "filename"."""
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


def save_projects_to_file(filename, projects):
    """Save projects to file "filename"."""
    with open(filename, 'w') as out_file:
        print(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects grouped by completion"""
    print("Incomplete projects")
    for project in projects:
        if not project.is_complete():
            print(f"\t{project}")
    print("Complete projects")
    for project in projects:
        if project.is_complete():
            print(f"\t{project}")


if __name__ == '__main__':
    main()
