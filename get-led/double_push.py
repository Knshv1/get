import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24]
num = 0
GPIO.setup(leds, GPIO.OUT)
sleep_time = 0.2
GPIO.output(leds, 0)
up = 10
down = 9
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
while True:
    if GPIO.input(up) and not GPIO.input(down):
        num = num + 1
        if num<=255:
            print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down) and not GPIO.input(up):
        num = num - 1
        if num >=0:
            print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(up) and GPIO.input(down):
        num = 255
        time.sleep(sleep_time)
    if num<0:
        num = 0
    if num > 255:
        num = 0
    GPIO.output(leds, dec2bin(num))
    time.sleep(sleep_time*5)