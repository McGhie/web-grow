#!/usr/bin/env python

def getfrompi():


	import time
	import serial
	#import sqlite3
	#conn = sqlite3.connect('example.db')

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

	if (counter<5):
		x=port.readline()
		if(x):
			text_file = open("templates/Output.txt", "a+")
			text_file.write(x+"\r\n")
			text_file.close()
		counter = counter + 1


def getfromlaptop():

	    # -*- coding: utf-8 -*-
	text_file = open("templates/arduino.html", "a+")
	text_file.write("\nDebug-Testing line\r\n")
	text_file.close()

def clearData():
		text_file = open("templates/arduino.html", "w")
		text_file.write("")
		text_file.close()
