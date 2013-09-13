#!/usr/bin/python
from __future__ import print_function
from pylab import *
from datetime import datetime, date
import time
import mysql.connector
import sys
import json
import requests
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('rpi-hygro.cnf')
dbuser = config.get('Database','user')
dbpass = config.get('Database','password')
dbhost = config.get('Database','host')
dbname = config.get('Database','schema')

try:
  cnx = mysql.connector.connect(user=dbuser, password=dbpass, host=dbhost, database=dbname)
except mysql.connector.errors.InterfaceError, msg:
  print("MySQL Connection Error: %s" % msg)
  sys.exit(1)

cursor = cnx.cursor()
query = ('''SELECT 
		time date,
		humidity hum,
		temperature temp
	FROM 
		sensor_readings
	WHERE 
		time > DATE_SUB(NOW(),INTERVAL 2 DAY)
	ORDER BY
		time''')
cursor.execute(query)

d = []
mhum = []
mtmp = []
for (date,xhum,xtemp) in cursor:
  d.append(date)
  mhum.append(xhum)
  mtmp.append(xtemp)
cursor.close()

uri = 'http://api.openweathermap.org/data/2.1/history/city/2751316?type=hour'

dat = requests.get(uri)
jdat = json.loads(dat.text)

wtime = []
whum = []
for wd in jdat['list']:
    wtime.append(datetime.fromtimestamp(int(wd['dt'])))
    whum.append(wd['main']['humidity'])

title('Humidity and Temperature')
grid(True)
p1 = plot_date(d, mhum, 'r-', label='Humidity')
p2 = plot_date(d, mtmp, 'b-', label='Temperature')
p3 = plot_date(wtime, whum, 'g-', label='Humidity OWM')
legend()
show()
