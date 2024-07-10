#! /usr/bin/env python3

import sqlite3 as sql
import argparse as argp

parser = argp.ArgumentParser(description="Database helper")

# handle arguments
parser.add_argument('--create', metavar='TABLENAME', type=str, help='Create a new table with the given table name')
parser.add_argument('--list-tables', action='store_true', help='List all tables in the database')

# parse incoming arguments to the script
args = parser.parse_args()


db = 'database.db'

if args.create:
    tablename = args.create
    print(f"Creating table <{tablename}>")
    try:
        conn = sql.connect(db)
        cur  = conn.cursor()
        print(f"Trying to create table with name: {tablename}")
        conn = sql.connect(db)
        create_query = """CREATE TABLE {} ( name text, phone text, email text)""".format(tablename)
        cur.execute(create_query)
        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Failed to create: {e}")
elif args.list_tables:
    conn = sql.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    conn.close()
    if tables:
        print(f"Found these tables in the database ({db})")
        for table in tables:
            print(" > " + table[0])
    else:
        print(f"Found no tables in the database ({db})")