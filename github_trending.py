import sys
import requests as r

if len(sys.argv) < 2:
    trending = 'https://github-trending-api.now.sh/repositories'
else:
    (language, since) = sys.argv[1:]
    trending = 'https://github-trending-api.now.sh/repositories?language={}&since={}'.format(language, since)

jsonX = r.get(trending)
name = []

try:
    jsonX = jsonX.json()

    for obj in jsonX:
        name.append(obj['name'])
except:
    print("Errorified!")

for x in name:
    print(x)


