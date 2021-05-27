import pandas as pd
import json
import csv
import matplotlib.pyplot as plt
import seaborn as sns
"%matplotlib inline"

#Load json data
with open(r"C:\Users\Mani\OneDrive\Documents\Manivel\HCL\python430\covid.json") as json_data:
    data=json.load(json_data)
    
#Write headers
field_headers=[]
for headers in data["fields"]:
    field_headers.append(headers["label"])

#Write data in csv file
with open(r"C:\Users\Mani\OneDrive\Documents\Manivel\HCL\python430\covidcsv.csv", "w") as csv_input:
    writer=csv.DictWriter(csv_input, fieldnames=field_headers)
    writer.writeheader()
    for values in data["data"]:
        writer.writerow({field_headers[0]:int(values[0]), field_headers[1]:values[1],field_headers[2]:int(values[2]),field_headers[3]:int(values[3]), field_headers[4]:int(values[4]),field_headers[5]:int(values[5])})
        
        
#Read CSV file using pandas:
df=pd.read_csv(r"C:\Users\Mani\OneDrive\Documents\Manivel\HCL\python430\covidcsv.csv")

#Print first five values of a dataframe
df.head()

#Print first 2 rows and columns using iloc
df.iloc[1:3,1:3]

#Print first 2 rows and columns using loc
df.loc[1:3,"District":"Active Cases as on 25.05.2021"]

#Print summary of a dataframe
summary=df.sum().transpose()

#Plot the covid data using matplotlib:

X = df.iloc[:,1] #District
Y = df.iloc[:,2] #Y* Total positive cases

plt.figure(figsize=(25,8))
  
ax = plt.axes()

#Grid length and color
ax.grid(linewidth=0.4, color='#8f8f8f') 
  
ax.set_facecolor("black")

#Set x-axis and y-axis 
ax.set_xlabel('\nDistrict',size=25,color='#4bb4f2')
ax.set_ylabel('Total Positive\n',size=25,color='#4bb4f2')

#PLot the graph 
ax.plot(X,Y,
        color='#1F77B4',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='#035e9b')