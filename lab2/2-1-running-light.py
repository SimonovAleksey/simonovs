import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds=[2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)
for i in range(3):
    for l in leds:
        GPIO.output(l, 1)
        time.sleep(0.2)
        GPIO.output(l, 0)
GPIO.output(leds, 0)
GPIO.cleanup()
