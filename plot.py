import matplotlib.pyplot as plt
import pandas as pd
d = pd.read_csv('energy.csv')
year = d['index']
sea_levels = d['kWh']
plt.plot(year, sea_levels)
plt.xlabel('Amostra')
plt.ylabel('Consumo (kWh)')
plt.title('Amostras de consumo de energia')
plt.show()
