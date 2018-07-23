#!/usr/bin/env python3

import records

db = records.Database('sqlite:///vets.db')

rows = db.query('''
    SELECT * 
    FROM gravesites
    WHERE state = 'California' AND
    burial_space = 'Open'
''')

print(rows.dataset)
