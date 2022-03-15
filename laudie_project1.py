#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:22:01 2022

@author: jesslaudie
"""

## Importing the packages that will be used

import requests
import pandas as pd
import sqlite3

## Assigning the API to a python object called url, to be used later

url = "http://hp-api.herokuapp.com/api/characters"

## Retrieving data from API and checking validty of connection

response = requests.get(url)

print(response.status_code)
print(response.json())

## Reading in the url as a pandas dataframe

df = pd.read_json(url)
df

## Retrieving info about current dataframe (column and row counts)

rows = len(df.axes[0])
cols = len(df.axes[1])

print("Number of Rows:", rows)
print("Number of Columns:", cols)


## Establishing a cursor connection if one does not exist (connecting to created database)

conn = sqlite3.connect('project_database')

if conn is not None:
    c = conn.cursor()
    

## Converting data in pandas dataframe into strings so it is compatible with sqlite

df = df.applymap(str)

## Converting pandas dataframe to sql table called harry_potter

df.to_sql('harry_potter', con=conn, if_exists = 'fail', index=False)

## Checking that the data was inserted into the harry_potter sql table

c.execute("SELECT * FROM harry_potter")
myresult = c.fetchall()
for x in myresult:
    print(x)
    
## Seeing how many columns there are in the harry_potter sql table
## This output gives us a descriptive list of the column names as well as an enumerated list to see the count

print('\nColumns in harry_potter table:')
data=c.execute('''SELECT * FROM harry_potter''')

try:
    for column in data.description:
        print(column[0])
    for column in enumerate(data.description):
            print(column[0])
except sqlite3.Error as error:
        print("Fail to count", error)
        

## We can see that there are 19 columns (0:18)

## Deleting selected columns from sql table and verifying that they were deleted

def deleteColumns():
    try: 
        c.execute("ALTER TABLE harry_potter DROP alternate_names")
        c.execute("ALTER TABLE harry_potter DROP dateOfBirth")
        c.execute("ALTER TABLE harry_potter DROP image")
        c.execute("ALTER TABLE harry_potter DROP wand")
        c.execute("ALTER TABLE harry_potter DROP alternate_actors")
        print('\nColumns in harry_potter table:')
        data=c.execute('''SELECT * FROM harry_potter''')
        for column in data.description:
            print(column[0])
    except sqlite3.Error as error:
        print("Failed to delete columns", error)
deleteColumns()
conn.commit()
conn.close()

## We can see that the columns were appropriately deleted
