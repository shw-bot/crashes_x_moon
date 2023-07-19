# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:33:47 2023

@author: cinshalewolfe
"""
import requests
import json
import sqlite3
import pandas as pd

r = requests.get('https://data.cincinnati-oh.gov/resource/rvmt-pkmq.json?$limit=1000&$offset=8000&$$app_token=Lj9QgGYRLWk8EtLtwO77SR8jL', verify=False)

data = r.text
parse = json.loads(data)

conn = sqlite3.connect(r'C:\Users\cinshalewolfe\Desktop\traffic_project\cin_traffic.db')
cursor = conn.cursor()

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

cursor.execute('''
               CREATE TABLE crashes_backup AS SELECT * FROM crashes
               ''')

conn.commit()
conn.close()
