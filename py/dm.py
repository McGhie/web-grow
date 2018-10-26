from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
#GPIO.output(12, GPIO.HIGH)

p = GPIO.PWM(12, 50)

p.start(100)

sleep(5)
p.ChangeDutyCycle(0)
p.stop()

GPIO.cleanup()
