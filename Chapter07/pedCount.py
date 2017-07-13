#! /usr/bin/python3

# import our libraries
from adxl345 import ADXL345
from time import sleep
import scrollphathd as shd
from scrollphathd.fonts import font3x5

# setup our variables and objects
adxl345 = ADXL345()
pedCnt = 0
Thresh = 1.15 # Change this to match your threshold
last_state = 'below'

# define two functions to display messages
def scrollMsgOnce(msg):
    msg = msg + "      " # 6 spaces
    buffer = shd.write_string(msg, x=17, y=0, brightness=0.5)
    for i in range(buffer):
        shd.show()
        shd.scroll(1)
        sleep(0.05)
    shd.clear()
    shd.show()

def showMsgOnce(msg):
    shd.clear()
    shd.show()
    shd.write_string(msg, x=0, y=1, font=font3x5, brightness=0.25)
    shd.show()

# clear our screen and display a welcome message
shd.clear()
shd.show()
scrollMsgOnce("Raspberry Pi Zero Pedometer!")
sleep(0.5)

# start counting our steps
while True:
    # get our axes reading
    axes = adxl345.getAxes(True)
    # set current_sate - above or below
    # starts as below
    current_state = last_state
    if axes['x'] < Thresh:
        # we are still below threshold
        current_state = 'below'
    elif axes['x'] > Thresh:
        # we have gone above threshold
        current_state = 'above'

    if current_state is not last_state:
        # we have a change in state
        if current_state is 'above':
            # that change is to go above
            # so increment count and display it
            pedCnt += 1
            showMsgOnce(str(pedCnt))
    
    # set last state to current
    last_state = current_state


