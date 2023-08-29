import sqlite3

def list():
    try:
        print("Listing tasks")
        # Connect to the database
        conn = sqlite3.connect("tareas.sql")
        cursor = conn.cursor()

        # Fetch tasks from the database
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        # Display tasks to the user
        for task in tasks:
            print(f"Task ID: {task[0]}\nTask Name: {task[1]}\nDueDate: {task[2]}\nStatus: {task[3]}\n")

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")

def add(task):
    try:
        # Connect to the database
        conn = sqlite3.connect("tareas.sql")
        cursor = conn.cursor()

        print(f"Adding task: {task}")
        query = "INSERT INTO tasks VALUES(54,'" + task + "','','')"
        cursor.execute(query)
        cursor.fetchone()

        conn.commit()
        print(f"Ready")

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")

def clear():
    try:
        # Connect to the database
        conn = sqlite3.connect("tareas.sql")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tasks WHERE tasks.id > 10")
        conn.commit()
        print(f"New records cleared")

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")