#! /usr/bin/python3

from adxl345 import ADXL345
from time import sleep 
from blinkt import set_clear_on_exit, set_pixel, show, set_brightness

adxl345 = ADXL345()

set_clear_on_exit()
set_brightness(0.1)

def adxlToRGB(axis):
    axes = adxl345.getAxes(True)
    absADXL = abs(axes[axis])
    if (absADXL >= 1):
        absADXL = 1
    rgbADXL = int(255 * absADXL)
    return rgbADXL

while True:
    for i in range(8):
        set_pixel(i, adxlToRGB("x"), adxlToRGB("y"), adxlToRGB("z"))
        show()
    axes = adxl345.getAxes(True)
    sleepY = abs(axes["y"]) / 50
    sleep(sleepY)
