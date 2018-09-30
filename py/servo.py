import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
servoPIN = 16
servoPower = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN,GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
twentymin = 1200
onehour = 3600



def basic():

      p.start(10)
      time.sleep(1.5)
      p.ChangeDutyCycle(1)
      time.sleep(1.5)
      p.ChangeDutyCycle(10)
      p.stop()
      GPIO.cleanup

def timer(duration):

      p.start(10)
      time.sleep(1.5)
      p.ChangeDutyCycle(1)
      time.sleep(duration)
      p.ChangeDutyCycle(10)
      p.stop()
      GPIO.cleanup
