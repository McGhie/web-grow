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

GPIO.output(16, GPIO.HIGH)
p = GPIO.PWM(12, 50)

p.start(100)
sleep(1)
GPIO.output(16, GPIO.LOW)


sleep(2)
p.ChangeDutyCycle(0)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
p.stop()

GPIO.cleanup()
