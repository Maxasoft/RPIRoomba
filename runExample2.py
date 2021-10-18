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

    # path to move
    for lft, rht, dt, s in path:
        move_robot(lft, rht, dt, s)

    print('shutting down ... bye')
    bot.drive_stop()
    time.sleep(0.1)
