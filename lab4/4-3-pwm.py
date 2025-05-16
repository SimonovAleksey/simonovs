import RPi.GPIO as GPIO

PWM_PIN = 24
PWM_FREQ = 1000
VCC = 3.3
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, PWM_FREQ)
pwm.start(0)

try:
    while True:
        duty_input = input("enter fill-koef: ")
        try:
            duty_cycle = int(duty_input)
            if 0 <= duty_cycle <= 100:
                pwm.ChangeDutyCycle(duty_cycle)
                u = VCC * duty_cycle / 100
                print(u, "- ожидаемое напряжение")
            else:
                print("значение от 0 до 100!")
        except ValueError:
            print("Введите целое число!")

finally:
    pwm.stop()
    GPIO.cleanup()
