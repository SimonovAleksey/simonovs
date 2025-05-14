import RPi.GPIO as gpio
import time
from matplotlib import pyplot

gpio.setmode(gpio.BCM)

leds=[21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)

dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)

comp=4
troyka=17 
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
    napr=0
    result_ismer=[]
    time_start=time.time()

   
    print('Начало зарядки конденсатора...')
    while napr<220:
        napr=adc()
        result_ismer.append(napr)
    


    gpio.setup(troyka,gpio.OUT, initial=gpio.LOW)

    print('Начало разрядки конденсатора...')
    while napr>40:
        napr=adc()
        result_ismer.append(napr)
    time_experiment=time.time()-time_start

    print('Запись данных в файл...')
    with open('data.txt', 'w') as f:
        for i in result_ismer:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/len(result_ismer)) + '\n')
        f.write('0.01289')
    
    print('Общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/len(result_ismer), 1/(time_experiment/len(result_ismer)), 0.013))

    
    print('Построение графиков...')
    y=[i/256*3.3 for i in result_ismer]
    x=[i*time_experiment/len(result_ismer) for i in range(len(result_ismer))]
    pyplot.plot(x, y)
    pyplot.xlabel('t, c')
    pyplot.ylabel('U, V')
    pyplot.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()
