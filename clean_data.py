import csv
import numpy as np
import tensorflow as tf
from formatDateTime import *

data = []
f = open('DATA.csv', 'r')
line = f.readline()
while line:
    data += [line.split(',')]
    line = f.readline()

data = np.array(data)

for row in range(len(data)):
    if row == 0: continue
    for col in range(len(data[row])):
        if col == 0 or col == 3 or col == 6:    # these cols in the dataset are ints
            #change type to int
            data[row][col] = int(data[row][col])
        if col == 5:    # this col in the dataset is a float
            #change type to float
            data[row][col] = float(data[row][col])
        if col == 4:
            data[row][col] = formatDateTime(data[row][col])
print data[1:10]

