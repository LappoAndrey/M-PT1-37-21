#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc
import sqlite3
from collections import namedtuple
import re
import sys
import os

usage = '''
py mdb2sqlite.py BMOFARM.MDB db.sqlite3
Usage: mdb2sqlite.py <input.mdb> <output.sqlite>
'''

filename_in = os.path.abspath(sys.argv[-2])
filename_out = sys.argv[-1]
print(filename_in)

#cnxn = pyodbc.connect('Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};PWD=k_i_ry_an;'.format(filename_in))
cnxn = pyodbc.connect('Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};UID=admin;Dbq={0};PWD=k_i_ry_an;CharacterSet=CP1251'.format(filename_in))



cursor = cnxn.cursor()

conn = sqlite3.connect(filename_out)

c = conn.cursor()

Table = namedtuple('Table', ['cat', 'schem', 'name', 'type'])

# get a list of tables
tables = []
for row in cursor.tables():
    if row.table_type == 'TABLE':
        t = Table(row.table_cat, row.table_schem, row.table_name, row.table_type)
        tables.append(t)

for t in tables:
    print(t.name)
    
    # SQLite tables must being with a character or _
    # t_name = t.name
    #if not re.match('[a-zA-Z\_]', t.name):
    t_name = 'app_' + t.name

    # get table definition
    columns = []
    for row in cursor.columns(table=t.name):
        print('    {} [{}({})]'.format(row.column_name, row.type_name, row.column_size))
        col_name = re.sub('[^a-zA-Z0-9]', '_', row.column_name)
        columns.append('{} {}({})'.format(col_name, row.type_name, row.column_size))
    cols = ', '.join(columns)
        
    # create the table in SQLite
    c.execute('DROP TABLE IF EXISTS "{}"'.format(t_name))
    c.execute('CREATE TABLE "{}" ({})'.format(t_name, cols))
    
    # copy the data from MDB to SQLite
    cursor.execute('SELECT * FROM "{}"'.format(t.name))
    for row in cursor:
        values = []
        for value in row:
            if value is None:
                values.append(u'NULL')
            else:
                if isinstance(value, bytearray):
                    value = sqlite3.Binary(value)
                else:
                    value = u'{}'.format(value)
                values.append(value)
        v = ', '.join(['?']*len(values))
        sql = 'INSERT INTO "{}" VALUES(' + v + ')'
        c.execute(sql.format(t_name), values)

conn.commit()
conn.close()