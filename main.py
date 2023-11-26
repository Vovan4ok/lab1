import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd


################################ПОБУДОВА ГРАФІКУ################################
def atmospheric_pressure(h, T):
    g = 9.8
    M = 0.028
    p0 = 101325
    R = 8.31
    p = p0 * math.exp(-((g * M * h) / (R * T)))
    return p

heights = np.arange(0, 1001, 10)
temperatures = np.arange(273, 334, 20)
colors = ['red', 'blue', 'purple', 'yellow']

for i in range(len(temperatures)):
    pressures = [atmospheric_pressure(h, temperatures[i]) for h in heights]
    plt.plot(pressures, heights, color=colors[i], label=f'Температура повітря {temperatures[i]}')

plt.title('Залежність атмосферного тиску від висоти')
plt.xlabel('Атмосферний тиск (Па)')
plt.ylabel('Висота над рівнем моря (м)')
plt.grid(True)
plt.legend()
plt.show()

################################ПОБУДОВА ГІСТОГРАМИ################################
heights = np.arange(0, 1001, 100)
pressures = [atmospheric_pressure(h, 273) for h in heights]
plt.figure()
plt.bar(heights, pressures, width=20, align='center', color='red')
plt.title("Гістограма залежності атмосферного тиску від висоти")
plt.xlabel("Висота над рівнем моря (м)")
plt.ylabel("Атмосферний тиск (Па)")
plt.grid(True)
plt.show()

################################ПОБУДОВА ТАБЛИЦІ################################
heights = np.arange(0, 1001, 100)
pressures1 = [atmospheric_pressure(h, 273) for h in heights]
pressures2 = [atmospheric_pressure(h, 293) for h in heights]
pressures3 = [atmospheric_pressure(h, 313) for h in heights]
table = {"Висота": heights, "273 К": pressures1, "293 К": pressures2, "313 К": pressures3}
table = pd.DataFrame(table)
print("Таблиця залежності атмосферного тиску від висоти та температури")
print(table)