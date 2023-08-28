import sqlite3
import database

database.initialize_database()

connection = sqlite3.connect("tareas.sql")
cursor = connection.cursor()
cursor.execute("""
            SELECT * FROM tasks
            """)
print(cursor.fetchmany(10))