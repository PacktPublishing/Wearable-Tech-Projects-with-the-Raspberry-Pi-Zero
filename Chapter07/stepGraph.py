#!/usr/bin/python3

from adxl345 import ADXL345
from time import sleep
import csv

adxl345 = ADXL345()

with open('steps.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(240):
        axes = adxl345.getAxes(True)
        writer.writerow([i + 1, axes['x']])
        sleep(0.125)
