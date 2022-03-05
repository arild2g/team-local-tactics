import sqlite3
from sqlite3 import Error

from core import Champion

def createConnection(database):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn


def selectAllChamps(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Champions")
    rows = cur.fetchall()
    
    champDict = {}
    for row in rows:
        champDict[row[0]] = Champion(row[0], row[1], row[2], row[3])

    return champDict


