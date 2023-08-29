import sqlite3

def add(task):
    # Connect to the database
    conn = sqlite3.connect("tareas.sql")
    cursor = conn.cursor()

    query = "INSERT INTO tasks VALUES(54,'" + task + "','','')"
    cursor.execute(query)
    cursor.fetchone()

    print(f"Ready")

    # Close the connection
    conn.commit()
    conn.close()