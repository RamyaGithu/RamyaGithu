import requests
import time
from playsound import playsound
from selenium import webdriver
from time import sleep

#https://apisetu.gov.in/public/api/cowin#/Metadata%20APIs/states - Govt API Site

#565 - Chengalpattu
#571 - Chennai

district_id= 571

date="09-06-2021"

#APT site to get vaccines available by district
url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(district_id, date)

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

#Using selenium to notify using whatsapp
driver=webdriver.Chrome(r"C:\Users\Mani\OneDrive\Documents\Manivel\HCL\python430\chromedriver.exe")
driver.get(r"https://web.whatsapp.com/")

#Method to check vaccine availability
def vaccineAvailability():
    count = 0
    response = requests.get(url=url, headers = header)
    response_json=response.json()
    data=response_json["sessions"]
    for d in data:
        if ((d["available_capacity"]>0) & (d["min_age_limit"] <=45) & (d["vaccine"] == "COVAXIN") & (d["available_capacity_dose2"]> 0)):
            count+=1
            available_data= d["name"]+"\n"+d["address"]+"\n"+"dose2:"+str(d["available_capacity_dose2"])+"\n"+d["vaccine"]
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format("Manivel"))
            user.click()
            text_box = driver.find_element_by_class_name('_2A8P4')
            text_box.send_keys(available_data)
            sleep(3)
            send_button = driver.find_element_by_class_name("EBaI7")
            send_button.click()
            playsound(r'C:\Users\Mani\OneDrive\Desktop\Interview\ding-sound.mp3') #Notify with a sound in the desktop once vaccine is found
            return True
    
    if count == 0:
        print("No Vaccines Available")
        return False


   

    
    
    
#Method calling in loop until we find vaccine availible   
while(vaccineAvailability != True):
    time.sleep(300)
    vaccineAvailability()