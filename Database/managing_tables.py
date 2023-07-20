# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:03:44 2023

@author: cinshalewolfe
"""

import sqlite3
import pandas as pd

# create connection to database
conn = sqlite3.connect('Databse\cin_traffic.db')
cursor = conn.cursor()

# drop columns we don't need
cursor.execute('ALTER TABLE crashes DROP COLUMN cpd_neighborhood')
cursor.execute('ALTER TABLE crashes DROP COLUMN instanceid')
cursor.execute('ALTER TABLE crashes DROP COLUMN localreportno')
cursor.execute('ALTER TABLE crashes DROP COLUMN roadclass')
cursor.execute('ALTER TABLE crashes DROP COLUMN roadclassdesc')
cursor.execute('ALTER TABLE crashes DROP COLUMN roadcontour')
cursor.execute('ALTER TABLE crashes DROP COLUMN roadsurface')
cursor.execute('ALTER TABLE crashes DROP COLUMN typeofperson')
cursor.execute('ALTER TABLE crashes DROP COLUMN datecrashreported')

# delete rows with null neighborhood values since we want to know that info
cursor.execute('''
               DELETE FROM crashes
               WHERE community_council_neighborhood = 'N/A'
               ''')

# split crashdate column into separate date and time columns

cursor.execute('ALTER TABLE crashes ADD COLUMN date')
cursor.execute('ALTER TABLE crashes ADD COLUMN time')
cursor.execute('''
               UPDATE crashes
               SET
               time = TRIM(substr(crashdate, instr(crashdate,'T')+2)),
               date = TRIM(substr(crashdate, 1, instr(crashdate,'T')-1))
               ''')

cursor.execute('''
               ALTER TABLE crashes DROP COLUMN crashdate
               ''')

#binary encode the gender column

cursor.execute('''
               UPDATE crashes
               SET
               gender = CASE
               WHEN gender = 'F - FEMALE' THEN 0
               ELSE 1
               END
               ''')

# create sql table from csv 
   
moon_phases = pd.read_csv('Database\moon_phases.csv')

cursor.execute('''
               CREATE TABLE moon_phases (
                   day TEXT,
                   date DATE,
                   moon_phase TEXT,
                   moon_sign TEXT,
                   modality TEXT,
                   element TEXT,
                   masc_fem TEXT,
                   body_part TEXT,
                   ruling_planet TEXT
               )
               ''')

moon_phases.to_sql('moon_phases', conn, if_exists='append', index=False)

#fill null values in table with correct values

cursor.execute('''
               UPDATE moon_phases
               SET ruling_planet = 'Mercury'
               WHERE ruling_planet IS NULL
               ''')

#join tables
               
cursor.execute('''
               CREATE TABLE IF NOT EXISTS crashes_x_moon AS
               SELECT *
               FROM crashes
               LEFT JOIN moon_phases ON crashes.date = moon_phases.date
                   
               ''')
               
cursor.execute('ALTER TABLE crashes_x_moon DROP COLUMN "date:1"')

conn.commit()
conn.close()






  


