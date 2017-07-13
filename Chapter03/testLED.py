#!/usr/bin/python3

from gpiozero import LED
from time import sleep

pair1 = LED(11)
pair2 = LED(9)
pair3 = LED(10)
pair4 = LED(7)
pair5 = LED(8)


for i in range(4):
    pair1.on()
    sleep(2)
    pair1.off()
    pair2.on()
    sleep(2)
    pair2.off()
    pair3.on()
    sleep(2)
    pair3.off()
    pair4.on()
    sleep(2)
    pair4.off()
    pair5.on()
    sleep(2)
    pair5.off()
