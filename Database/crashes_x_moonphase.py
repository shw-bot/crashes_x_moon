import sqlite3
import pandas as pd
from sklearn import preprocessing

# create connection to database

conn = sqlite3.connect('YOUR_DATABASE_FILEPATH.db')
cursor = conn.cursor()

query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM crashes_x_moon
                               ''', conn)

# create a dataframe from the table

crashes_x_moon = pd.DataFrame(query)

conn.commit()
conn.close()

# let's do a little clean-up

crashes_x_moon['age'] = crashes_x_moon['age'].fillna(crashes_x_moon['age'].median())

crashes_x_moon[['hundred_block', 'road']] = crashes_x_moon['address_x'].apply(lambda x: pd.Series(str(x).split("XX")))


# label-encode the hierarchical columns

label_encoder = preprocessing.LabelEncoder()
crashes_x_moon['crashseverity']= label_encoder.fit_transform(crashes_x_moon['crashseverity'])
crashes_x_moon['injuries']= label_encoder.fit_transform(crashes_x_moon['injuries'])

# split the address column so we have the street names and numbers separate

for idx, x in enumerate(crashes_x_moon['address_x']):
    if ('I7' not in x) and ('SR5' not in x) and 'XX' in x:
        crashes_x_moon.at[idx, 'hundred_block'], crashes_x_moon.at[idx, 'road'] = str(x).split("XX", 1)
    else:
        crashes_x_moon.at[idx, 'road'] = x

# drop original column and fill null values

crashes_x_moon = crashes_x_moon.drop('address_x', axis=1)
crashes_x_moon['hundred_block'] = crashes_x_moon['hundred_block'].fillna(0)
crashes_x_moon['hundred_block'] = crashes_x_moon['hundred_block'].replace('', 0)

# create a csv file for tableau visualization

crashes_x_moon.to_csv('Database\crashes_x_moon.csv')


        


