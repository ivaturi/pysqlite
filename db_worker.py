import sqlite3 as sql

class Database:
    
    def __init__(self, name):
        self.db = name

    def create_table(self, tablename):
        query =  """CREATE TABLE {} ( name text, phone text, email text)""".format(tablename)
        conn = sql.connect(self.db)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()
    
    def get_tables(self):
        query = "select name from sqlite_master where type='table';"
        conn = sql.connect(self.db)
        cur = conn.cursor()
        cur.execute(query)
        tables = cur.fetchall()
        conn.close()
        return tables if tables else False