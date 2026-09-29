import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
tnow = 0



if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], amplitude, True)

        while True:
            c = sg.get_sin_wave_amplitude(signal_frequency, tnow) * amplitude
            
            dac.set_voltage(c)
            sg.wait_for_sampling_period(sampling_frequency)
            tnow = tnow + (1/sampling_frequency)
    finally:
        dac.deinit()