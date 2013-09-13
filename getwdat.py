#!/usr/bin/python
import datetime
import requests
import json

uri = 'http://api.openweathermap.org/data/2.1/history/city/2751316?type=hour'

dat = requests.get(uri)
jdat = json.loads(dat.text)

for d in jdat['list']:
    dtime = datetime.datetime.fromtimestamp(int(d['dt']))
    dhum = d['main']['humidity']
    print("dt: %s, hum: %s" % (dtime,dhum))
