import requests
import time
from playsound import playsound

#https://apisetu.gov.in/public/api/cowin#/Metadata%20APIs/states - Govt API Site

#565 - Chengalpattu

district_id= 565

date="07-06-2021"

url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(district_id, date)

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def vaccineAvailability():
    count = 0
    response = requests.get(url=url, headers = header)
    response_json=response.json()
    data=response_json["sessions"]
    for d in data:
        if ((d["available_capacity"]>0) & (d["min_age_limit"] >18)):
            count+=1
            print(d["name"])
            print(d["address"])
            print("Dose1:",d["available_capacity_dose1"])
            print("Dose2:",d["available_capacity_dose2"])
            print(d["vaccine"])
            playsound(r'C:\Users\Mani\OneDrive\Desktop\Interview\ding-sound.mp3')
            return True
    
    if count == 0:
        print("No Vaccines Available")
        return False
    
    
    
while(vaccineAvailability != True):
    time.sleep(5)
    vaccineAvailability()