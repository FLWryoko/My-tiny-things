from pathlib import Path
from array import array
import csv
import matplotlib.pyplot as pyplot
import numpy as np

print('path to csv file')
pathname = input()
fpath  = Path(pathname)
file = Path.open(fpath)
dreader = csv.DictReader(file)
x =array('f')
y =array('f')

for row in dreader:
    print('row:x  '+row['x'])
    print('row:y  '+row['y'])
    x.append(float(row['x']))
    y.append(float(row['y']))
fig,ax = pyplot.subplots()
ax.plot(x,y)
pyplot.show()
