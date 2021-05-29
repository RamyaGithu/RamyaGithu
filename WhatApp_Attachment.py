from selenium import webdriver
from time import sleep

#To get Chrome Drive path 
driver=webdriver.Chrome(r"C:\Users\Mani\OneDrive\Documents\Manivel\HCL\python430\chromedriver.exe")

#To get web whatapp browser in chrome; Then scan with your QR code for login into webbrowser 
driver.get(r"https://web.whatsapp.com/")

#Attachment to be sent to particular user in whatsapp
whatappname=input("Enter the name of the user ")
filepath=input("Enter file path ") #C:\Users\Mani\OneDrive\Desktop\CovidTN.png

#Checks given whatsapp name using inspect
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(whatappname))
user.click()

#To get location of attachment button
attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attachment_box.click()

#Attachs the given image in photos & videos
image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

#Send the image or video to given user in whatapp
send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()