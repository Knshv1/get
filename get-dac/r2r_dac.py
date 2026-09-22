import RPi.GPIO as GPIO
import time

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.out, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def voltage_to_number(voltage):
        if not(0.0<=voltage<=dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            return(0)
        return int(voltage/ dynamic_range *255)
    def number_to_dac(number):
        a = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(leds, a)