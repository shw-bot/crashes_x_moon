import sqlite3
import pandas as pd
import numpy as np
from sklearn import preprocessing


conn = sqlite3.connect('Database\cin_traffic.db')
cursor = conn.cursor()

query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM crashes_x_moon
                               ''', conn)

crashes_x_moon = pd.DataFrame(query)

conn.commit()
conn.close()

#let's do a little clean-up

crashes_x_moon['age'] = crashes_x_moon['age'].fillna(crashes_x_moon['age'].median())

crashes_x_moon[['hundred_block', 'road']] = crashes_x_moon['address_x'].apply(lambda x: pd.Series(str(x).split("XX")))


#label-encode the hierarchical columns
label_encoder = preprocessing.LabelEncoder()
crashes_x_moon['crashseverity']= label_encoder.fit_transform(crashes_x_moon['crashseverity'])
crashes_x_moon['injuries']= label_encoder.fit_transform(crashes_x_moon['injuries'])

#split the address column so we have the street names available
for idx, x in enumerate(crashes_x_moon['address_x']):
    if ('I7' not in x) and ('SR5' not in x) and 'XX' in x:
        crashes_x_moon.at[idx, 'hundred_block'], crashes_x_moon.at[idx, 'road'] = str(x).split("XX", 1)
    else:
        crashes_x_moon.at[idx, 'road'] = x

crashes_x_moon = crashes_x_moon.drop('address_x', axis=1)
crashes_x_moon['hundred_block'] = crashes_x_moon['hundred_block'].fillna(0)
crashes_x_moon['hundred_block'] = crashes_x_moon['hundred_block'].replace('', 0)

crashes_x_moon.to_csv('Database\crashes_x_moon.csv')


        


