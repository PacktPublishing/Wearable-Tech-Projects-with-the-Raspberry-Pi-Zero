#! /usr/bin/python3

from twython import Twython

# import our access tokens from the auth.py file
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# make a connection to twitter
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# send a hello world tweet
message = "Hello world from my first Python tweet!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
