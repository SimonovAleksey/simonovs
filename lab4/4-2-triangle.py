import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(x) for x in bin(value)[2:].zfill(8)]
def setper():
    while True:
        try:
            period = float(input("set period: "))
            if period <= 0:
                print("must be > 0!")
                continue
            return period
        except ValueError:
            print("must be number!")
try:
    period = setper()
    half = period/2
    step = half/255
    while True:
        for i in range(256):
            GPIO.output(dac, dec2bin(i))
            time.sleep(step)
        for i in range(254, 0, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(step)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
