def trian(freq, time):
    phase = (time * freq) % 1.0
    return abs(1.0 - 2.0 * phase)