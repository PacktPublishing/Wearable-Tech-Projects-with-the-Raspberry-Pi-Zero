#!/usr/bin/python3

from gpiozero import LED, Button

btn = Button(25)
green = LED(23)
red = LED(14)

while True:
    btn.wait_for_press()
    green.blink(0.5,0.5)
    red.blink(0.25,0.25)
    btn.wait_for_press()
    green.off()
    red.off()
