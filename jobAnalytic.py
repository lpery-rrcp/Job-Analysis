import sqlite3


def add_job(title, company, date):
    """This function adds Job components to the SQL.
            - Job title
            - Company
            - Date applied
        (Can add more later but the above are essential.)
    """
    application = [title, company, date]
    con = sqlite3.connect("JobApplicationData.db")
    cur = con.cursor()

    # Checks to see if table is created if not makes it
    cur.execute('''CREATE TABLE IF NOT EXISTS jobapplications
                    (id INTEGER PRIMARY KEY, title TEXT NOT NULL, company TEXT NOT NULL, date_applied TEXT NOT NULL)
                ''')

    # Insert data
    cur.execute(
        """INSERT INTO jobapplications (title, company, date_applied) VALUES (?, ?, ?)""", application)

    con.commit()
    new_id = cur.lastrowid
    con.close()

    return f"Job Added: {title} | ID: {new_id}"


def delete_job(id: int):
    """Deletes the entire job application (not the table)"""
    con = sqlite3.connect("JobApplicationData.db")
    cur = con.cursor()

    # Deletes data
    cur.execute("""DELETE FROM jobapplications WHERE id = ?""", (id,))

    con.commit()
    con.close()
    return f"Removed Job {id}"


def clear_job():
    pass


def edit_job():
    """
    Edit different variables to the job application.
            - Job Title
            - Company
            - Date Applied
    """
    con = sqlite3.connect("JobApplicationData.db")
    cur = con.cursor()

    con.commit()
    con.close()
    return "Job edited"


def show_database():
    con = sqlite3.connect("JobApplicationData.db")
    cur = con.cursor()

    cur.execute("""SELECT * FROM jobapplications""")
    rows = cur.fetchall()

    con.close()
    return rows


while True:
    print("1. Add Job Application.")
    print("2. Delete Job Application")
    print("3. Edit Job Application")
    print("4. Show database")
    print("5. Clear Database")
    print("6. Exit")
    userInput = int(input("Enter number: "))

    if userInput == 1:
        print(add_job("Cain", "CnA", "2017-05-20"))
    elif userInput == 2:
        print(delete_job(1))
    elif userInput == 3:
        print(edit_job())
    elif userInput == 4:
        print(show_database())
    elif userInput == 5:
        print(clear_job())
    elif userInput == 5:
        print("Thanks for using Job Analytics.❤️")
        break
    else:
        print("Invalid entry!! Please use numbers.")
