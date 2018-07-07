#!/usr/bin/env python

import time
import serial

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
	x.ser.readline()
	if(x):
		print x
