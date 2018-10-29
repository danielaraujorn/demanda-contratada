from datetime import datetime
from datetime import timedelta
import random
from math import exp
import csv
import sys
date = datetime.now()
with open('energy.csv', 'w', newline='') as csvfile:
    fieldnames = ['index', 'date', 'kWh']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(int(sys.argv[1])):
        writer.writerow({'index': i, 'date': date+timedelta(seconds=(30*i+random.randint(0, 10)-5)),
                         'kWh':  exp(random.uniform(0, 10))})
