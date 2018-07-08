#!/usr/bin/env python

def getfrompi():


	import time
	import serial
	#import sqlite3
	#conn = sqlite3.connect('example.db')

	port =serial.Serial(
		"/dev/ttyUSB0",
		baudrate=9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		writeTimeout = 10,
		timeout = 10,
		rtscts=False,
		dsrdtr=False,
		xonxoff=False
	)


	x=port.readline()
	if(x):
		text_file = open("templates/arduino.html", "a+")
		text_file.write(x)
		text_file.close()
	


def getfromlaptop():

	    # -*- coding: utf-8 -*-
	text_file = open("templates/arduino.html", "a+")
	text_file.write("\nDebug-Testing line\r\n")
	text_file.close()

def clearData():
		text_file = open("templates/arduino.html", "w")
		text_file.write("")
		text_file.close()
