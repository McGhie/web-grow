import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
on = 'on'

# Create a dictionary called pins to store the pin number, type, and pin state:
pins = {
   1 : {'type' : '3.3v', 'state' : on},
   2 : {'type' : '5v', 'state' : on},
   3 : {'type' : 'GPIO 02', 'state' : GPIO.LOW},
   4 : {'type' : '5v', 'state' : on},
   5 : {'type' : 'GPIO 03', 'state' : GPIO.LOW},
   6 : {'type' : 'Ground', 'state' : GPIO.LOW},
   7 : {'type' : 'GPIO 04', 'state' : GPIO.LOW},
   8 : {'type' : 'GPIO 14', 'state' : GPIO.LOW},
   9 : {'type' : 'Ground', 'state' : GPIO.LOW},
   10 : {'type' : 'GPIO 15', 'state' : GPIO.LOW},
   11 : {'type' : 'GPIO 17', 'state' : GPIO.LOW},
   12 : {'type' : 'GPIO 18', 'state' : GPIO.LOW},
   13 : {'type' : 'GPIO 27', 'state' : GPIO.LOW},
   14 : {'type' : 'Ground', 'state' : GPIO.LOW},

   }
