#! /usr/bin/env python3

import argparse as argp
from db_worker import Database

parser = argp.ArgumentParser(description="Database helper")

# handle arguments
parser.add_argument('--create', metavar='TABLENAME', type=str, help='Create a new table with the given table name')
parser.add_argument('--list-tables', action='store_true', help='List all tables in the database')

# parse incoming arguments to the script
args = parser.parse_args()

db = Database('database.db')


if args.create:
    tablename = args.create
    print(f"Creating table <{tablename}>")
    db.create_table(tablename)
  
elif args.list_tables:
    tables = db.get_tables()
    if tables:
        print(f"Found these tables...")
        for table in tables:
            print(" > " + table[0])
    else:
        print(f"Found no tables")



