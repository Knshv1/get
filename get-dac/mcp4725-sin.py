import mcp4725_driver as mcp
import time
import math
import RPi.GPIO as GPIO
import signal_generator as sg

amplitude = 2.0
sfreq = 10
samplfreq = 1000
dynamic_range = 3.183
dac = mcp.MCP4725(dynamic_range, verbose= False)

try:
    start = time.time()
    period = 1/samplfreq
    next = start
    
    while True:
        try:
            t = time.time() - start
            s = sg.get_sin_wave_amplitude(sfreq, t) * amplitude
            #s = amplitude / 2* (1 + math.sin(2 * math.pi * sfreq * t))
            dac.set_voltage(s)
            next += period
            sleep = next - time.time()
            
            if sleep > 0:
                time.sleep(sleep)
        except ValueError:
            print('')
finally:
    dac.deinit()
    print("")