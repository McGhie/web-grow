import os
import time
arm = True

if (os.uname()[4].startswith("arm")): #check if system is pi if not use fake pins
    import RPi.GPIO as GPIO
    import pinboard
    DEBUG = False
    GPIO.setwarnings(False)
    waterPin = 12
    servoPower = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPIN,GPIO.OUT)


else:
    arm = False




twentymin = 1200
onehour = 3600

if (arm):

    def basic():
          print('Water basic')
          GPIO.output(waterPin, GPIO.HIGH)
          time.sleep(20)
          GPIO.output(waterPin, GPIO.LOW)
          GPIO.cleanup
          print('Checkpoint cleanup')

    def timer(duration):

          p.start(10)
          time.sleep(1.5)
          p.ChangeDutyCycle(1)
          time.sleep(duration)
          p.ChangeDutyCycle(10)
          p.stop()
          GPIO.cleanup

else:

    def basic():
          print('Water basic')
          time.sleep(20)
          print('Checkpoint water cleanup')

    def timer(duration):
          print('Checkpoint basic')
          time.sleep(1.5)
          print('Checkpoint 1.5')
          time.sleep(duration)
          print('Checkpoint sleep' + duration)
