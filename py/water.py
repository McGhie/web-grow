import os
import time
arm = True

if (os.uname()[4].startswith("arm")): #check if system is pi if not use fake pins
    import RPi.GPIO as GPIO
    import pinboard
    DEBUG = False
    GPIO.setwarnings(False)
    waterPin = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(waterPin,GPIO.OUT)


else:
    arm = False

if (arm):

    def basic():
          print('Water basic')
          GPIO.output(waterPin, GPIO.HIGH)
          time.sleep(600)
          GPIO.output(waterPin, GPIO.LOW)
          GPIO.cleanup
          print('Checkpoint cleanup')

    def timer(t):
          print('Water basic')
          GPIO.output(waterPin, GPIO.HIGH)
          time.sleep(t)
          GPIO.output(waterPin, GPIO.LOW)
          GPIO.cleanup
          print('Checkpoint cleanup')


else:

    def basic():
          print('Water basic')
          time.sleep(20)
          print('Checkpoint water cleanup')
