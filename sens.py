#!/usr/bin/python
from sht1x.Sht1x import Sht1x as SHT1x
from Adafruit_CharLCD import Adafruit_CharLCD
from time import localtime, strftime, sleep
import RPi.GPIO as GPIO

dataPin = 7
clkPin = 12

while True:

  # Get data from SHT11
  GPIO.setmode(GPIO.BOARD)
  sht1x = SHT1x(dataPin, clkPin)
  temperature = sht1x.read_temperature_C()
  humidity = sht1x.read_humidity()
  try:
    dewPoint = sht1x.calculate_dew_point(temperature, humidity)
  except ValueError, msg:
    print("Error calculating dew point: %s" % msg)

  # Format time
  curtime = strftime("%H:%M", localtime())

  # Setup LCD
  lcd = Adafruit_CharLCD()
  lcd.clear()
  # \xDF = degree symbol for LCD display

  # Show the data
  lcd.message("T: {:2.2f}\xDFC H: {:2.2f}%\nD: {:2.2f}\xDFC T: {}".format(temperature, humidity, dewPoint, curtime))
  # print("T: {:2.2f}\xC2\xB0C H: {:2.2f}%\nD: {:2.2f}\xB0C T: {}".format(temperature, humidity, dewPoint, curtime))
  print("Time: {} Temperature: {:2.2f}\xC2\xB0C Humiditiy: {:2.2f}% Dew Point: {:2.2f}\xC2\xB0C".format(curtime, temperature, humidity, dewPoint))
  
  # Flush output, needed to get output if ran with nohup 
  sys.stdout.flush()

  sleep(60)
