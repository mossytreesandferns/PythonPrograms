# Python SQLite: 3 ways to enter data into a database

import pandas as pd
import sqlite3 as lite
import csv as csv
import sys

barcelona_csv = pd.read_csv('/Users/meganporter/OwnJupyterNotebooks/BarcelonaDataSet/barcelona-data-sets/population.csv')


class fakeBarcelona():

    def __init__(self,year,districtCode,districtName,neighborhoodCode, neighborhoodName,gender,age,number):

        self.year = year
        self.districtCode = districtCode
        self.districtName = districtName
        self.neighborhoodCode = neighborhoodCode
        self.neighborhoodName = neighborhoodName
        self.gender = gender
        self.age = age
        self.number = number

database = lite.connect('Barcelona.db')

curs = database.cursor()


# Entering rows by hand

curs.execute("""CREATE TABLE population (
    year integer,
    districtCode integer,
    districtName text,
    neighborhoodCode integer, 
    neighborhoodName text,
    gender text,
    age integer,
    number integer 
    )""")


curs.execute("INSERT INTO Population VALUES(4453,2367,'FakeDistrict2', 1010,'FakeNeighborhoodName2', 'gender', 164, 123 )")



# Using a class object

tuala =  fakeBarcelona(1989, 1234, "tualaville", 4444, "Tamoshanter", "Female", 122, 332)
 

curs.execute("INSERT INTO Population VALUES(:year, :districtCode, :districtName, :neighborhoodCode, :neighborhoodName, :gender, :age, :number)",
{'year':tuala.year, 'districtCode': tuala.districtCode, 'districtName': tuala.districtName, 'neighborhoodCode': tuala.neighborhoodCode, 
'neighborhoodName': tuala.neighborhoodName, 'gender': tuala.gender, 'age': tuala.age, 'number': tuala.number})


# Importing a csv

barcelona_csv = open('/Users/meganporter/OwnJupyterNotebooks/BarcelonaDataSet/barcelona-data-sets/population.csv')
csv_reader = csv.reader(barcelona_csv, delimiter=',',quotechar='"')

for line in csv_reader:
    curs.execute('INSERT INTO population VALUES (?,?,?,?,?,?,?,?)',line)

barcelona_csv.close()



curs.execute("select * from Population")
print(curs.fetchall(10))

database.commit() 
database.close()


