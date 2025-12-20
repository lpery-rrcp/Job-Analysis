import sqlite3


def add_job():
    """This function adds Job components to the SQL.
            - Job title
            - Company
            - Date applied
        (Can add more later but the above are essential.)
    """

    return "Job Added"


def delete_job():
    """Deletes the entire job application"""
    return "Removed Job"


def edit_job():
    """
    Edit different variables to the job application.
            - Job Title
            - Company
            - Date Applied
    """
    return "Job edited"


print("1. Add Job Application.")
print("2. Delete Job Application")
print("3. Edit Job Application")
print("4. Exit")
userInput = int(input("Enter number: "))

if userInput == 1:
    print(add_job())
elif userInput == 2:
    print(delete_job())
elif userInput == 3:
    print(edit_job())
elif userInput == 4:
    print("Thanks for using Job Analytics.❤️")
else:
    print("Invalid entry!! Please use numbers.")
