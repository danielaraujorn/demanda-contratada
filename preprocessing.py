import pandas as pd
from datetime import datetime
from datetime import timedelta
import random
from math import exp
import csv

date = datetime.now()
d = pd.read_csv('energy.csv', delimiter=";", low_memory=False)

dates = d['Date']
times = d['Time']
active_powers = d['Global_active_power']
active_reactive_powers = d['Global_reactive_power']


def toTimeStamp(ldate, ltime):
    return (datetime.strptime(ldate + ' ' +
                              ltime, '%d/%m/%Y %H:%M:%S')).timestamp()


with open('energyNew.csv', 'w', newline='') as csvfile:
    fieldnames = ['Index', 'Datetime',
                  'Global_active_power', 'Global_reactive_power']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i, (date, time, activepower, reactivepower) in enumerate(zip(dates, times, active_powers, active_reactive_powers)):
        if(activepower != '?'):
            writer.writerow({'Index': i, 'Datetime': int(toTimeStamp(date, time)),
                             'Global_active_power': float(activepower), 'Global_reactive_power': float(reactivepower)})
