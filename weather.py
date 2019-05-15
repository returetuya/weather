import requests
import json
import datetime
from pytz import timezone
import os
import sys

apikey='*****************'
cities="169-0072,JP"

api= 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}'


num1= input("西暦を教えてください(ex.2018)")
num2=input("何月か教えてください(ex.04)")
num3=input("何日か教えてください(ex.01)")
num4=input("時間を教えてください(ex.12)")

x,y,z,l=int(num1),int(num2),int(num3),int(num4)
def gettenki():
   url =api.format(cities,apikey)
   r= requests.get(url)
   data=json.loads(r.text)



   if not ('list' in data):
       print('error')
       return

   for ten in data['list']:

       weatherDescription = ten['weather'][0]['description']
       forecastDatetime = datetime.datetime.fromtimestamp(ten['dt'])
       temperature = ten['main']['temp']
       rainfall=0

       if 'rain' in ten and '3h' in ten['rain']:
           rainfall = ten['rain']['3h']

        zikoku = [tenki for tenki in ten if [x,y,z,l] in forecastDatetime]

        print('日時:{0} 天気:{1} 気温(℃):{2} 雨量(mm):{3}'.format(
           zikoku, weatherDescription, temperature, rainfall))

       
