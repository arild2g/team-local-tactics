import sqlite3
from sqlite3 import Error
from core import Champion, Match

def createConnection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn

def selectAllChamps(conn):
    cur = conn.cursor()
    cur.execute("select * from Champions")
    rows = cur.fetchall()
    
    champDict = {}
    for row in rows:
        champDict[row[0]] = Champion(row[0], row[1], row[2], row[3])

    return champDict

def saveMatchToDatabase(conn, match: Match):
    cur = conn.cursor()
    cur.execute(f"insert into Match values({match.score[0]},{match.score[1]});")
    conn.commit()