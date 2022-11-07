"""
CP1404 | project and project management | Liam Eime
Estimate time = 1.5hrs
Actual time =
"""

import datetime
from prac_07.project import Project
from operator import attrgetter

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
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
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
            start_date = get_date_from_string(parts[1])
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
            date_to_string(project)
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects grouped by completion"""
    print("Incomplete projects")
    for project in projects:
        date_to_string(project)
        if not project.is_complete():
            print(f"\t{project}")
    print("Complete projects")
    for project in projects:
        date_to_string(project)
        if project.is_complete():
            print(f"\t{project}")


def filter_projects_by_date(projects):
    """Filter projects by date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = get_date_from_string(date_string)
    projects.sort(key=attrgetter('start_date'))
    for project in projects:
        date_to_string(project)
        if get_date_from_string(project.start_date) >= date:
            print(project)


def add_new_project(projects):
    """Add new project to projects"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def get_date_from_string(date_string):
    """Get date from string"""
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()


def date_to_string(project):
    """Make date string if not string"""
    if not isinstance(project.start_date, str):
        project.start_date = project.start_date.strftime("%d/%m/%Y")


if __name__ == '__main__':
    main()
