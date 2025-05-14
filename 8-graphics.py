from matplotlib import pyplot as plt
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker


with open('/Users/aleksey/Documents/pythonProject/VCP/settings.txt') as file:
    settings = [float(i) for i in file.read().split('\n') if i] 
data = np.loadtxt('/Users/aleksey/Documents/pythonProject/VCP/data.txt', dtype=int) * settings[1]
data_time = np.array([i*(settings[0]) for i in range(data.size)])

max_voltage = np.max(data)
min_voltage = np.min(data)

charge_start_idx = np.where(data >= min_voltage)[0][0]
charge_end_idx = np.where(data == max_voltage)[0][0]

discharge_end_idx = np.where(data <= min_voltage + max_voltage)[0][-1]
charge_time = data_time[charge_end_idx] - data_time[charge_start_idx]
discharge_time = data_time[discharge_end_idx] - data_time[charge_end_idx]

fig, ax = plt.subplots(figsize=(16, 10), dpi=600)
ax.axis([data_time.min(), data_time.max()+1, data.min()-0.2, data.max()+0.5])

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC цепи', 70)), loc='center')
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")
time_info = (f"Время зарядки: {charge_time:.2f} с\n"
             f"Время разрядки: {discharge_time:.2f} с\n")
props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray', pad=0.5)
ax.text(0.98, 0.15, time_info, transform=ax.transAxes,
        fontsize=11, verticalalignment='top', horizontalalignment='right',
        bbox=props)

marker_freq = 70
marker_color='red'
marker_style='s'
marker_size=6

ax.plot(data_time[::marker_freq], data[::marker_freq], marker=marker_style, color=marker_color, markersize=marker_size, linestyle='None')
ax.grid(which='major', color='k')
ax.minorticks_on()
ax.grid(which='minor', color='blue', linestyle=':')
ax.plot(data_time, data, c='blue', linewidth=1, label='V(t)')
ax.legend(shadow=True, loc='upper right', fontsize=12)

fig.savefig('graph.png')
fig.savefig('graph.svg')
fig.show()
print('Генерация графика завершена.')