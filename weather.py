import requests
import json
import datetime
from pytz import timezone
import os
import sys
import re

apikey='***************'
cities="169-0072,JP"

api= 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}'

k2c=lambda k:k-272.15

def gettenki():
    url =api.format(cities,apikey)
    r= requests.get(url)
    data=json.loads(r.text)
    
    if not ('list' in data):
        print('error')
        return
    
    for tenki in data['list']:
        
        forecastDatetime = datetime.datetime.fromtimestamp(tenki['dt'])
        rainfall=0
        weatherDescription = tenki['weather'][0]['description']
        temperature = tenki['main']['temp']
        weather_info ={}
        weather_info['日時'] = forecastDatetime
        
        weather_list = []
        weather_list.append(weather_info)
        
        if 'rain' in tenki and '3h' in tenki['rain']:
            rainfall = tenki['rain']['3h']
            weather_info['日時'] = forecastDatetime
    
    return weather_list
    



# num1= input("いつの天気が知りたいですか？（ex.20190817）")

# from datetime import datetime as dt
# adt = dt.strptime(num1, '%Y%m%d')
# newstr = adt.strftime('%Y-%m-%d')
# print(newstr)


# import re
#for row in weather_list:
 #   re.findall(adt, row)

