import RPi.GPIO as GPIO
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2bin(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]
try:
    while True:
        number = input('Введите число от 0 до 255')
        if number == "q":
            exit()
        try:
            if int(number) > 255:
                print("Число должно быть до 255!")
            elif int(number) < 0:
                print("Число должно быть положительным!")
        except ValueError:
            try: 
                if float(number):
                    print("Число не должно быть типа float!")  
            except ValueError:
                print("Вы ввели строку... Введите число!")
        else:
            GPIO.output(dac, decimal2bin(int(number)))
            print("{:.4f}".format(int(number)/256*3.3))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
