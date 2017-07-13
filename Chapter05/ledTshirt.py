#! /usr/bin/python3

# import our libraries
from gpiozero import LEDBoard
from random import randint
from time import sleep

# to listen to Twitter we need the TwythonStreamer library
from twython import TwythonStreamer

# import our access tokens from the auth.py file
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# define our LEDBoards
redLEDs = LEDBoard(15, 18, 17, 27)
greLEDs = LEDBoard(14, 2, 3, 4)
bluLEDs = LEDBoard(23, 24, 22, 25)
allLEDs = LEDBoard(redLEDs, greLEDs, bluLEDs)

# define our LED sparkle function
def sparkleLED(board, loop):
    for i in range(loop):
        board.on()
        sleep(randint(10,25)/100)
        board.off()
        sleep(randint(10,25)/100)

# set our hashtags to search for
TERMS = ['#SparkleRed', '#SparkleBlue', '#SparkleGreen', '#MultiSparkle']

# adapt the TwythonStreamer class
class TshirtStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            if '#SparkleRed' in data['text']:
                sparkleLED(redLEDs, randint(5, 20))
            elif '#SparkleBlue' in data['text']:
                sparkleLED(bluLEDs, randint(5, 20))
            elif '#SparkleGreen' in data['text']:
                sparkleLED(greLEDs, randint(5, 20))
            else:
                sparkleLED(allLEDs, randint(5, 20))

# connect with our streamer class
stream = TshirtStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track=TERMS)
