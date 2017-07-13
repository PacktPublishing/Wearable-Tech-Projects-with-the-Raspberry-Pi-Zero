#!/usr/bin/python3
from gpiozero import Button, LED
from signal import pause
from time import sleep
from os import system

button = Button(21, hold_time=3)
led = LED(16)

def shutdown_piZero():
    for i in range(3):
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
    system("sudo shutdown now -hP")

button.when_held = shutdown_piZero
pause()
