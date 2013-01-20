#!/usr/bin/python
from __future__ import print_function
from pylab import *
from datetime import datetime, date, time
import mysql.connector
import sys
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('rpi-hygro.cnf')
dbuser = config.get('Database','user')
dbpass = config.get('Database','password')
dbhost = config.get('Database','host')
dbname = config.get('Database','schema')

try:
  cnx = mysql.connector.connect(user=dbuser, password=dbpass, host=dbhost, database=dbname)
except mysql.connector.Error, msg:
  print("MySQL Connect Error: %s" % msg)
  sys.exit()

cursor = cnx.cursor()
query = ('''SELECT HOUR(time) hour, MINUTE(time) minute, MIN(humidity) h_min, MAX(humidity) h_max, AVG(humidity) h_avg FROM sensor_readings GROUP BY HOUR(time),minute(time)''')
cursor.execute(query)

hmin = []
hmax = []
havg = []
t = []
for (dhour,dminute,h_min,h_max,h_avg) in cursor:
  hmin.append(h_min)
  hmax.append(h_max)
  havg.append(h_avg)
  a = datetime(int(2000),int(1),int(1),int(dhour),int(dminute))
  t.append(matplotlib.dates.date2num(a))
cursor.close()

cursor = cnx.cursor()
query = ('''SELECT HOUR(time) hour, MINUTE(time) minute, AVG(humidity) h_avg FROM sensor_readings WHERE time > NOW() - INTERVAL 1 DAY GROUP BY HOUR(time),minute(time)''')
cursor.execute(query)

todayhavg = []
todayt = []
for (dhour,dminute,h_avg) in cursor:
  todayhavg.append(h_avg)
  a = datetime(int(2000),int(1),int(1),int(dhour),int(dminute))
  todayt.append(matplotlib.dates.date2num(a))
cursor.close()


title('Humidity per hour')
grid(True)
p1 = plot_date(t, hmin, 'r-', label='Min Humidity')
p2 = plot_date(t, hmax, 'b-', label='Max Humidity')
p2 = plot_date(t, havg, 'g-', label='Avg Humidity')
p2 = plot_date(todayt, todayhavg, 'y-', label='Avg Humidity 24h')
legend()
show()
