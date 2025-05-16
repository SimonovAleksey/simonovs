import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def bintrans(s):
    return [int(b) for b in bin(s)[2:].zfill(8)]
try:
    while True:
        a = input()
        if a == 'q':
            break
        try:
            n = int(a)
            if not 0 <= n <= 255:
                print("Число должно быть от 0 до 255!")
                continue
            bins = bintrans(n)
            GPIO.output(dac, bins)
            U = (n/255)*3.3
            print(f"Напряжение: {U:.2f} Вольт")
        except ValueError:
            print("Значение должно быть целым числом!")
except KeyboardInterrupt:
    print("0")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
