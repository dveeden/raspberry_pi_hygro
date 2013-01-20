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
except mysql.connector.errors.InterfaceError, msg:
  print("MySQL Connection Error: %s" % msg)
  sys.exit(1)

cursor = cnx.cursor()
query = ('''SELECT 
		time date,
		CONCAT(LPAD(HOUR(time),2,"0"), ":", LPAD(MINUTE(time),2,0)) time,
		humidity,
		temperature
	FROM 
		sensor_readings
	GROUP BY 
		DATE(time),
		HOUR(time),
		FLOOR(MINUTE(time) / 10)''')
cursor.execute(query)

d = []
h = []
temp = []
for (date,time,humidity,temperature) in cursor:
  d.append(date)
  h.append(humidity)
  temp.append(temperature)
cursor.close()

title('Humidity and Temperature')
grid(True)
p1 = plot_date(d, h, 'r-', label='Humidity')
p2 = plot_date(d, temp, 'b-', label='Temperature')
legend()
show()
