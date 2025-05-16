import RPi.GPIO as GPIO
from time import sleep
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2bin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]
try:
    while (True):
        number = input()
        if number == "q":
            exit()
        elif not number.isdigit():
            print("Введите число, а не строку!")
        timepause=int(number)/256/2
        for i in range(256):
            GPIO.output(dac, decimal2bin(i))
            sleep(timepause)
        for i in range(254, 0, -1):
            GPIO.output(dac, decimal2bin(i))
            sleep(timepause)  
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
