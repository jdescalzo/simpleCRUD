import sqlite3
import pandas as pd

sample_data = "sample.csv"

def initialize_database():
    # Crea una conexión a la base de datos
    connection = sqlite3.connect("tareas.sql")

    # Crea un cursor, que permite ejecutar sentencias SQL
    cursor = connection.cursor()

    try:
        cursor.execute('''
            CREATE TABLE tasks (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                DueDate DATETIME,
                Status TEXT
            )
        ''')
    except:
        pass

    try:
        # Crea un dataframe de los datos en CSV y los interta en la tabla
        df =  pd.read_csv("sample.csv")
        df.to_sql("tasks", connection, if_exists='append', index=False)
        connection.commit()
        connection.close()
    except:
        pass