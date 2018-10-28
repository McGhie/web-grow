from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)

sleep(1)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)
sleep(1)

print ("setting pump on")
p = GPIO.PWM(12, 50)

p.start(100)

i = 1
while i < 20:
  sleep(10)
  print(i)
  i += 1

GPIO.output(18, GPIO.LOW)
p.stop()
GPIO.cleanup()
