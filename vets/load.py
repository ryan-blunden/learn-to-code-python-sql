#!/usr/bin/env python3

import records
import tablib

gravesites_csv = tablib.Dataset().load(open('data/vets-gravesite-locations-usa.csv').read())

db = records.Database('sqlite:///vets.db')

db.query('DROP TABLE IF EXISTS gravesites')
db.query('''
    CREATE TABLE gravesites (
      key int PRIMARY KEY, name text, address text, state text, contact text, burial_space text
    )
''')

key = 1
for gravesite in gravesites_csv.dict:
    name = gravesite['Cemetery Name']
    address = gravesite['Address']
    state = gravesite['State']
    contact = gravesite['Contact']
    burial_space = gravesite['Burial Space']

    db.query(
        'INSERT INTO gravesites (key, name, address, state, contact, burial_space) VALUES(:key, :name, :address, :state, :contact, :burial_space)',
        key=key, name=name, address=address, state=state, contact=contact, burial_space=burial_space
    )

    key += 1

print('[info]: Successfully imported {} records.'.format(key))
