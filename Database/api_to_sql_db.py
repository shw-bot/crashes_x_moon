# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:33:47 2023

@author: shalewolfe
"""
import requests
import json
import sqlite3
import config

# requestion a connection to the crash data API

api_token = config.API_TOKEN

r = requests.get('https://data.cincinnati-oh.gov/resource/rvmt-pkmq.json?$limit=1000&$offset=8000&$$app_token={api_token}', verify=False)

# load json data

data = r.text
parse = json.loads(data)

# create a connection to sql database

conn = sqlite3.connect('YOUR_DATABASE_FILEPATH.db')
cursor = conn.cursor()

# create sql table to load json data into

cursor.execute('''
               CREATE TABLE IF NOT EXISTS crashes(
               address_x TEXT,
               age Integer,
               community_council_neighborhood TEXT,
               cpd_neighborhood TEXT,
               crashdate TEXT,
               crashseverity TEXT,
               crashseverityid Integer,
               datecrashreported TEXT,
               dayofweek TEXT,
               gender TEXT,
               injuries TEXT,
               instanceid TEXT,
               latitude_x NUMERIC,
               lightconditionsprimary TEXT,
               localreportno Integer,
               longitude_x NUMERIC,
               mannerofcrash TEXT,
               roadclass Integer,
               roadclassdesc TEXT,
               roadconditionsprimary TEXT,
               roadcontour TEXT,
               roadsurface TEXT,
               sna_neighborhood TEXT,
               typeofperson TEXT,
               unittype TEXT,
               weather TEXT,
               zip Integer) ;
               '''
               )

columns = ['address_x', 'age', 'community_council_neighborhood', 'cpd_neighborhood',
           'crashdate', 'crashseverity', 'crashseverityid', 'datecrashreported', 
           'dayofweek', 'gender', 'injuries', 'instanceid', 'latitude_x',
           'lightconditionsprimary', 'localreportno', 'longitude_x',
           'mannerofcrash', 'roadclass', 'roadclassdesc', 'roadconditionsprimary', 
           'roadcontour', 'roadsurface', 'sna_neighborhood', 'typeofperson',
           'unittype', 'weather', 'zip']

for idx, row in enumerate(parse):
    keys = tuple(row.get(c, None) for c in columns)
    placeholders = ', '.join(['?' for _ in range(len(columns))])
    query = f'INSERT INTO crashes VALUES ({placeholders})'
    cursor.execute(query, keys)
    print(f'Row {idx + 1} data inserted Successfully')

# create back-up table

cursor.execute('''
               CREATE TABLE crashes_backup AS SELECT * FROM crashes
               ''')

conn.commit()
conn.close()
