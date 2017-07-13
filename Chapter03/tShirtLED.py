#!/usr/bin/python3

from gpiozero import LEDBoard
from time import sleep
from random import randint

leds = LEDBoard(11, 9, 10, 7, 8)

while True:
    for i in range(5):
        wait = randint(5,10)/10
        leds.on()
        sleep(wait)
        leds.off()
        sleep(wait)
    for i in range(5):
        wait = randint(5,10)/10
        leds.value = (1, 0, 1, 0, 1)
        sleep(wait)
        leds.value = (0, 1, 0, 1, 0)
        sleep(wait)
    for i in range(5):
        wait = randint(1,5)/10
        leds.value = (1, 0, 0, 0, 0)
        sleep(wait)        
        leds.value = (1, 1, 0, 0, 0)
        sleep(wait)        
        leds.value = (1, 1, 1, 0, 0)
        sleep(wait)        
        leds.value = (1, 1, 1, 1, 0)
        sleep(wait)        
        leds.value = (1, 1, 1, 1, 1)
        sleep(wait)
        leds.value = (1, 1, 1, 1, 0)
        sleep(wait)
        leds.value = (1, 1, 1, 0, 0)
        sleep(wait)
        leds.value = (1, 1, 0, 0, 0)
        sleep(wait)
        leds.value = (1, 0, 0, 0, 0)
        sleep(wait)

