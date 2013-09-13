#!/usr/bin/python
from __future__ import print_function
from pylab import *
from datetime import datetime, date
import time
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
		min(humidity) mihum,
		max(humidity) mahum,
		avg(humidity) ahum,
		min(temperature) mitmp,
		max(temperature) matmp,
		avg(temperature) atmp
	FROM 
		sensor_readings
	GROUP BY 
		WEEK(time)''')
cursor.execute(query)

d = []
mihum = []
mahum = []
ahum = []
mitmp = []
matmp = []
atmp = []
for (date,xmihum,xmahum,xahum,xmitmp,xmatmp,xatmp) in cursor:
  d.append(date)
  mihum.append(xmihum)
  mahum.append(xmahum)
  ahum.append(xahum)
  mitmp.append(xmitmp)
  matmp.append(xmatmp)
  atmp.append(xatmp)
cursor.close()

title('Humidity and Temperature')
grid(True)
p1 = plot_date(d, mihum, 'r-', label='Min Humidity')
p2 = plot_date(d, mahum, 'g-', label='Max Humidity')
p3 = plot_date(d, ahum, 'b-', label='Avg Humidity')
p4 = plot_date(d, mitmp, 'r-', label='Min Temperature')
p4 = plot_date(d, matmp, 'g-', label='Max Temperature')
p4 = plot_date(d, atmp, 'b-', label='Avg Temperature')
legend()
show()
