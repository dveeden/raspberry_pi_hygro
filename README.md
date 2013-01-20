Overview
========
This code will read the temperature and humidity. The results will
be printed and stored in a MySQL database. There are a few graphs
based on the data in the database.

Setup
=====
The setup I created this project for is the following:
- Raspberry Pi (rev 2)
- SHT11 Humidity & Temperature sensor
- 20x2 LCD HD44780 Compatible 

Download
========
To download the code with git:

  git clone git@github.com:dveeden/raspberry_pi_hygro.git

Configuration
=============
Copy the rpi-hygro.cnf.sample to rpi-hygro.cnf and adjust the settings 
to your configuration.

Data Collection
===============
The sens.py must be ran by root:

  nohup sudo ./sens.py &

Graphs
======
Run graph-min-max.py and/or graph-overview.py. This must 
be done on a machine wich can access the database.

Requirements
============
On the database macine:
- MySQL (Tested with 5.5)

On the machine which does the collection:
- Python
- MySQL Connector/Python
- Adafruit CharLCD
- rpiSht1x

On the machine which generates the graphs:
- Python
- MySQL Connector/Python
- matplotlib

References
==========
- http://shop.tuxgraphics.org/electronic/detail_sht11.html
- http://shop.tuxgraphics.org/electronic/detail_lcd_20x2.html
- http://pypi.python.org/pypi/rpiSht1x
- https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
- https://dev.mysql.com/doc/relnotes/connector-python/en/index.html
- http://matplotlib.org/
