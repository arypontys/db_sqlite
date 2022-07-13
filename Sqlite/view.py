import sqlite3 as lite


def commit_close(func):
    def decorator(*args):
        con = lite.connect('dados.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

@commit_close
def db_insert(name, phone, email):
    return """
    INSERT INTO users(name, phone, email) VALUES('{}', '{}', '{}')
        """.format(name, phone, email)


@commit_close
def db_update(name, email):
    return """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name, email)

@commit_close
def db_delete(email):
    return """
    DELETE FROM users WHERE email='{}'
    """.format(email)


def db_select(data, field):
    con = lite.connect('base.db')
    cur = con.cursor()
    sql = """
            SELECT * FROM users WHERE {}={}""".format(data, field)
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data