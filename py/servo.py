import os
import time
arm = True

if (os.uname()[4].startswith("arm")): #check if system is pi if not use fake pins
    import RPi.GPIO as GPIO
    import pinboard
    DEBUG = False
    GPIO.setwarnings(False)
    servoPIN = 16
    servoPower = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPIN,GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)

else:
    arm = False




twentymin = 1200
onehour = 3600

if (arm):

    def basic():
          print('Checkpoint basic')
          p.start(10)
          time.sleep(1.5)
          p.ChangeDutyCycle(1)
          time.sleep(1.5)
          p.ChangeDutyCycle(10)
          p.stop()
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
          print('Checkpoint basic')
          time.sleep(1.5)
          print('Sleep 1')
          time.sleep(1.5)
          print('Sleep 2')
          print('Checkpoint cleanup')

    def timer(duration):
          print('Checkpoint basic')
          time.sleep(1.5)
          print('Checkpoint 1.5')
          time.sleep(duration)
          print('Checkpoint sleep' + duration)
