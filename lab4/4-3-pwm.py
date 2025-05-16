import RPi.GPIO as GPIO
GPIO.setmode(gpio.BCM)
GPIO.setup(24, GPIO.OUT)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)
pwm = GPIO.PWM(24, 1000)
GPIO.start(0)
try:
    while True:
        try:
            DC = input()
            pwm.ChangeDutyCycle(int(DC))
            print("{:.2f}".format(int(DC)*3.3/100))
finally:
    pwm.stop()
    GPIO.cleanup()   
