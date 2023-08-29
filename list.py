import sqlite3

def list():
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

    # Close the connection
    conn.close()