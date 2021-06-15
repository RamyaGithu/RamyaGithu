import os
from datetime import *
import shutil

#Base path
path = r"C:\Users\Mani\OneDrive\Pictures"

#Method to name subfolder loaction wise based on year and month
def subFolderBasedOnLocation(stat_mtime):
    location=""
    year,month=stat_mtime.split(",")   
    if year == "2019" and month== "Jun":
        location ="Kodaikanal"
    elif year == "2021" and month== "Jun":
        location ="Ooty"
    else:
        location=month
    return year, location
    

# iterate through all file in base path
for file in os.listdir(path):
    if file.endswith(".jpg"):
        stat_info=os.stat(f"{path}\{file}")
        stat_mtime=datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y,%b')
        year,location=subFolderBasedOnLocation(stat_mtime) #Method calling
        os.makedirs(f"{path}\{year}\{location}")
        shutil.move(f"{path}\{file}", f"{path}\{year}\{location}\{file}")
    else:
        print(file, "Not a jpg Image file")
      
      
  
        


