import sqlite3

def clear():
    # Connect to the database
    conn = sqlite3.connect("tareas.sql")
    cursor = conn.cursor()

    # Fetch tasks from the database
    cursor.execute("DELETE FROM tasks WHERE tasks.id > 10")

    # Close the connection
    conn.commit()
    conn.close()