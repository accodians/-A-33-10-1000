import numpy as np
import sounddevice as sd
import time
wherearewe = 0
text = input("what would you like to say?")
t = np.arange(int(44100 * 0.5)) / 44100
while True:
    ascii = [ord(char) for char in text]
    frequency = (ascii[wherearewe]-33)*10+1000
    print(frequency)
    wave = np.sin(2 * np.pi * frequency * t)
    sd.play(wave, 44100)
    sd.wait()
    wherearewe = (wherearewe + 1) % len(ascii)
