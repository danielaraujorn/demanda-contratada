import matplotlib.pyplot as plt
from matplotlib.pyplot import axhline
from matplotlib.pyplot import axvline
import pandas as pd
import sys
d = pd.read_csv('energy.csv',  low_memory=False)
values = d['Global_active_power']
index = d['Index']
plt.plot(index, values)
plt.xlabel('Amostra')
plt.ylabel('Consumo (kWh)')
plt.title('Amostras de consumo de energia')
if(len(sys.argv) > 1):
    axhline(y=float(sys.argv[1]), color='red')
    # axvline(1025768, color='red')
    # axvline(1025783, color='red')
plt.show()
