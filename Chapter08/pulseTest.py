#!/usr/bin/python3

from envirophat import analog
from time import sleep

while True:
    pulse = analog.read(0)
    print("Pulse Voltage = {0}".format(pulse))
    sleep(0.25)
