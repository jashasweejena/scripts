import requests as r
import sys

(lat, long) = sys.argv[1:]

try:
    reqJson = r.get('https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}&zoom=18&addressdetails=1'.format(lat, long))

    if(reqJson.status_code == 200):
        reqJson = reqJson.json()

    print(reqJson['display_name'])
except:
    print("Invalid latitude and longitude")
