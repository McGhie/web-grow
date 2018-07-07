#!/usr/bin/env python
try:
	import time
	import serial
	import sqlite3
	conn = sqlite3.connect('example.db')

except: # -*- coding: utf-8 -*-
	text_file = open("templates/arduino.html", "w")
	text_file.write("\nnothin\n")
	text_file.close()


def getArduino():


		port =serial.Serial(
			"/dev/ttyUSB0",
			baudrate=57600,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
			writeTimeout = 0,
			timeout = 10,
			rtscts=False,
			dsrdtr=False,
			xonxoff=False
		)

		counter=0;

		while 1:
			x=port.readline()
			if(x):
				text_file = open("templates/Output.txt", "w")
				text_file.write(x)
				text_file.close()
