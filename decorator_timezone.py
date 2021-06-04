from datetime import datetime
import pytz

#Decorator function calling code
def worldTimeZone(func):
    def getTimeZone(country):
        if country != "Asia/Kolkata":
            country_tz         =pytz.timezone(country)
            country_datetime   =datetime.now(country_tz)
            country_tz_fmt     = country_datetime.strftime("%m/%d/%Y, %H:%M%p")
        else:
            country_tz_fmt= func(country)
        return country_tz_fmt
    return getTimeZone

@worldTimeZone
def checkTimeZone(country):
    now=datetime.now()
    current_time=now.strftime("%m/%d/%Y, %H:%M%p")
    return current_time
  
    
#Code input & execution:
country=input("Enter name of the time zone: ")   #eg: Asia/Kolkata, America/New_York
country_timezone=checkTimeZone(country) 
print(("Current_Time for {}:{}").format(country, country_timezone))
#Output:Current_Time for America/New_York: 06/04/2021, 01:52AM
