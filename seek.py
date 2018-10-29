import pandas as pd
from datetime import datetime

d = pd.read_csv('energy.csv',  low_memory=False)
janelaDeTempo = 15*60
dates = d['Datetime']
powers = d['Global_active_power']
length = len(dates)
demanda = 0.0
end = 0
start = 0

for i, (date, value) in enumerate(zip(dates, powers)):
    if(value != '?' and float(value) > demanda and i != length):
        j = i+1
        startLocal = i
        endLocal = j
        demandaLocal = float(powers[i])
        while dates[j]-date <= janelaDeTempo:
            endLocal = j
            if float(powers[j]) < demandaLocal:
                startLocal = start
                endLocal = end
                demandaLocal = demanda
                break
            if j == length:
                break
            j += 1
        demanda = demandaLocal
        start = startLocal
        end = endLocal
print(demanda, start, end)
