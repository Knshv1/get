import numpy as np
import time
def get_sin_wave_amplitude(freq, time):
    f = freq
    t = time
    a = np.sin(2*np.pi * f * t )
    b = a+1 
    c = b/2
    return(c)
def wait_for_sampling_period(sampling_frequency):
    ts = 1/sampling_frequency
    time.sleep(ts)