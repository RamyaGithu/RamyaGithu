from zipfile import *
import re
import csv
import json

# Zip file creation
zipper = ZipFile("pyzip.zip","w", ZIP_DEFLATED)
zipper.write("covidcsv.csv")
zipper.write("covid.json")
zipper.write("CovidTN.jpg")
zipper.close()

def csv_reader(i):
    with open(i,"r") as f:
        file = csv.reader(f)
        for line in file:
            for data in line:
                print(data)
                
def json_reader(i):
    with open(i,"r") as f:
        file = json.load(f)
        for line in file["data"]:
            print(line)

#Reading csv,json and image file using regex

zipper = ZipFile("pyzip.zip","r", ZIP_STORED)
files =   zipper.namelist()
            
for i in files:
    print(i)
    if re.search(".csv", i):
        csv_reader(i)          
    elif re.search(".json", i):
        json_reader(i)
    else:
        with open(i,"rb") as f: # Reading image file
            file=f.read()
            


           
            
