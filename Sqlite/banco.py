import sqlite3 as lite

con = lite.connect('dados.db')

cur = con.cursor()


def db_create():
    return """
        CREATE TABLE IF NOT EXISTS funcionario (matricula INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            cpf TEXT NOT NULL,
                            cargo TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL
                            )"""


cur.execute(db_create()) 
con.commit()
con.close()