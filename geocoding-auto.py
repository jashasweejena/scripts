import requests as r

reqIp = r.get('http://ipinfo.io')

if reqIp.status_code == 200:
    reqIp = reqIp.json()


lat = reqIp['loc'].split(',')[0]
long = reqIp['loc'].split(',')[1]

reqAddress = r.get('https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}&zoom=18&addressdetails=1'.format(lat, long))

if reqAddress.status_code == 200:
    reqAddress = reqAddress.json()

print(reqAddress['display_name'])