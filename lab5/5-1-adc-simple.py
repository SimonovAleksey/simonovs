import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2bin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]
def adc():
    for a in range(256):
        u = decimal2bin(a)
        GPIO.output(dac, u)
        compvalue = GPIO.input(comp)
        sleep(0.001)
        if compvalue == 1:
            return a
            
try:
    while True:
        a = adc()
        if a != 0:
            if a == None:
                a=255
            else:
                print(a, '{:.2f}v'.format(3.3*a/256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()   
