import requests as r
import sys

lat = input('Enter latitude')
long = input('Enter longitude')

reqJson = r.get('https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}&zoom=18&addressdetails=1'.format(lat, long))

if(reqJson.status_code == 200):
    reqJson = reqJson.json()

print(reqJson['display_name'])
