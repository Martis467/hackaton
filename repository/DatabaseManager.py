import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def querry_database(sql):
    conn = create_connection("randomizer.db")
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    return rows


def insert_to_database(sql, task):
    conn = create_connection("randomizer.db")
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()