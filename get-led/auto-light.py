import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
lig = 6
GPIO.setup(lig, GPIO.IN)
state = 0
while True:
    if GPIO.input(lig):
        state = 0
    else:
        state = 1
    GPIO.output(led, state)
    time.sleep(0.2)