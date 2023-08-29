import sqlite3

def list():
    try:
        print("Listing tasks")
        # Connect to the database
        conn = sqlite3.connect("tareas.sql")
        cursor = conn.cursor()
        print("Connected to SQLite")

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
        print("Connected to SQLite")

        print(f"Adding task: {task[1]}")
        values = tuple(task)
        sqlite_insert_with_param = """INSERT INTO tasks
                                  (ID, Name, DueDate) 
                                  VALUES (?, ?, ?);"""
        cursor.execute(sqlite_insert_with_param, values)

        query = """UPDATE tasks SET Status = "In Progress" WHERE ID = """ + str(task[0])
        cursor.execute(query)

        conn.commit()
        print(f"Ready")

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")

def complete(task):
    try:
        # Connect to the database
        conn = sqlite3.connect("tareas.sql")
        cursor = conn.cursor()
        print("Connected to SQLite")

        name_query = """SELECT Name FROM tasks WHERE ID = """ + str(task)
        cursor.execute(name_query)
        name = cursor.fetchone()
        print(f"Completing task: {name[0]}")

        query = """UPDATE tasks SET Status = "Completed" WHERE ID = """ + str(task)
        cursor.execute(query)

        conn.commit()
        print(f"Task Completed")

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
        print("Connected to SQLite")

        cursor.execute("DELETE FROM tasks WHERE tasks.id > 10")
        conn.commit()
        print(f"New records cleared")

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")