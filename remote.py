#!/usr/bin/env python3
#-*-coding:utf-8-*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
# moves the roomba through a simple sequence

import pycreate2
import time
from getkey import getkey, keys

def move_robot(lft, rht, dt, s):
    print(s)
    bot.digit_led_ascii(s)
    bot.drive_direct(lft, rht)
    time.sleep(dt)
    return

if __name__ == "__main__":
    # Create a Create2 Bot
    port = '/dev/ttyUSB0'  # this is the serial port on my raspberry pi
    baud = {
        'default': 115200,
        'alt': 19200  # shouldn't need this unless you accidentally set it to this
    }

    bot = pycreate2.Create2(port=port, baud=baud['default'])

    # define a movement path
    path = [
        [ 200, 200, 3, 'for'],
        [-200,-200, 3, 'back'],
        [   0,   0, 1, 'stop'],
        [ 100,   0, 2, 'rite'],
        [   0, 100, 4, 'left'],
        [ 100,   0, 2, 'rite'],
        [   0,   0, 1, 'stop'],
        [-200,-200, 3, 'back'],
        [-100, 100, 1, 'rite'],
        [ 100,-100, 1, 'left'],
        [   0,   0, 1, 'stop'],
        [ 100,-100, 1, 'left'],
        [-100, 100, 1, 'rite'],
        [   0,   0, 1, 'stop'],
        [   0,   0, 1, 'bye']
    ]

    bot.start()
    bot.safe()

    done = False
    while not done:
        key = getkey()
        if key in ['q', 'Q']:
            move_robot(100, 0, 1, 'fl')
        elif key in ['w', 'W']:
            move_robot(100, 100, 1, 'forw')
        elif key in ['e', 'E']:
            move_robot(0, 100, 1, 'fr')
        elif key in ['a', 'A']:
            move_robot(100, -100, 1, 'left')
        elif key in ['s', 'S']:
            move_robot(0, 0, 1, 'stop')
        elif key in ['d', 'D']:
            move_robot(-100, 100, 1, 'rite')
        elif key in ['z', 'Z']:
            move_robot(-100, 0, 1, 'bl')
        elif key in ['x', 'X']:
            move_robot(-100, -100, 1, 'back')
        elif key in ['c', 'C']:
            move_robot(0, -100, 1, 'br')
        elif key in ['p', 'P']:
            done = True

    print('shutting down ... bye')
    bot.drive_stop()
    time.sleep(0.1)
