import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2bin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, decimal2bin(k))
        time.sleep(0.001)
        if gpio.input(comp)==0:
            k-=2**i
    return k
def adc1():
    value = 128
    gpio.output(dac, decimal2bin(value))
    if gpio.input(comp) == 0:
        value -= 64
    else:
        value += 64
    gpio.output(dac, decimal2bin(value))
    if gpio.input(comp) == 0:
        value -= 32
    else:
        value += 32
    gpio.output(dac, decimal2bin(value))

    if gpio.input(comp) == 0:
        value -= 16
    else:
        value += 16
    gpio.output(dac, decimal2bin(value))
    if gpio.input(comp) == 0:
        value -= 8
    else:
        value += 8
    gpio.output(dac, decimal2bin(value))
    if gpio.input(comp) == 0:
        value -= 4
    else:
        value += 4
    gpio.output(dac, decimal2bin(value))
    if gpio.input(comp) == 0:
        value -= 2
    else:
        value += 2
    gpio.output(dac, decimal2bin(value))
    if gpio.input(comp) == 0:
        value -= 1
    else:
        value += 1
    gpio.output(dac, decimal2bin(value))
    return value

try:
    while True:
        a = adc1()
        if a == None:
            a = 255
        else:
            print(a, '{:.2f}v'.format(3.3*a/256))
             
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()    
