#!/usr/bin/python
from sht1x.Sht1x import Sht1x as SHT1x
from Adafruit_CharLCD import Adafruit_CharLCD
from time import localtime, strftime, sleep
import RPi.GPIO as GPIO
import sys
import mysql.connector
from mysql.connector import errorcode

dataPin = 7
clkPin = 12


interval=60
totalcount=(20*60)/interval
count = 0


while True:
  # Get data from SHT11
  # GPIO.setmode(GPIO.BOARD)
  sht1x = SHT1x(dataPin, clkPin)
  temperature = sht1x.read_temperature_C()
  humidity = sht1x.read_humidity()
  try:
    dewPoint = sht1x.calculate_dew_point(temperature, humidity)
  except ValueError, msg:
    print("Error calculating dew point: %s" % msg)

  # Format time
  curtime = strftime("%H:%M", localtime())
  curdate = strftime("%Y-%m-%d", localtime())

  # Setup LCD
  lcd = Adafruit_CharLCD()
  lcd.clear()
  # \xDF = degree symbol for LCD display

  # Show the data
  lcd.message("T: {:2.2f}\xDFC H: {:2.2f}%\nD: {:2.2f}\xDFC T: {}".format(temperature, humidity, dewPoint, curtime))
  # print("T: {:2.2f}\xC2\xB0C H: {:2.2f}%\nD: {:2.2f}\xB0C T: {}".format(temperature, humidity, dewPoint, curtime))
  print("Date: {} Time: {} Temperature: {:2.2f}\xC2\xB0C Humiditiy: {:2.2f}% Dew Point: {:2.2f}\xC2\xB0C".format(curdate, curtime, temperature, humidity, dewPoint))
  
  # Flush output, needed to get output if ran with nohup
  sys.stdout.flush()



  if count < totalcount:
    count += 1 
  else:
    count = 0

    try:
# make connection with mysql, error handeling
      conn = mysql.connector.connect(user="user", passwd="password", db="database")
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCES_DENIED_ERROR:
        print ("Wrong username or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print ("Wrong database name")
      else:
        print (err)

# put data in database
    cursor = conn.cursor()
    add_data = ("insert into sensor_readings (temperature, humidity) values (%s, %s)")
    sensor_data = (temperature, humidity)
    cursor.execute(add_data, sensor_data)

# commit data and close connection with mysql
    conn.commit()
    cursor.close()
    conn.close()

  sleep(interval)

