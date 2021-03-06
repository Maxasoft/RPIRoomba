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

CONST_FORWARD_LEFT  = 0
CONST_FORWARD       = 1
CONST_FORWARD_RIGHT = 2
CONST_ROTATE_LEFT   = 3
CONST_STOP          = 4
CONST_ROTATE_RIGHT  = 5
CONST_BACK_LEFT     = 6
CONST_BACK          = 7
CONST_BACK_RIGHT    = 8

def move_robot(lft, rht, dt, s):
    print(s)
    bot.digit_led_ascii(s)
    bot.drive_direct(lft, rht)
    time.sleep(dt)
    return

def calc_speed(key, speed):
    if key == 'o':
        if speed < 6:
            speed = speed + 1
    elif key == 'l':
        if speed > 1:
            speed = speed - 1
    return speed

def turn_robot(direction, speed):
    if direction == CONST_FORWARD_LEFT:
        l = speed * 50
        r = speed * 25
        m = 'fl' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_FORWARD:
        l = r = speed * 50
        m = 'f' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_FORWARD_RIGHT:
        l = speed * 25
        r = speed * 50
        m = 'fr' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_ROTATE_LEFT:
        l = speed * 50
        r = speed * -50
        m = 'l' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_STOP:
        speed = 1
        l = 0
        r = 0
        m = 's' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_ROTATE_RIGHT:
        l = speed * -50
        r = speed * 50
        m = 'r' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_BACK_LEFT:
        l = speed * -50
        r = speed * -25
        m = 'bl' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_BACK:
        l = speed * -50
        r = speed * -50
        m = 'bk' + str(speed)
        move_robot(l, r, 1, m)
    elif direction == CONST_BACK_RIGHT:
        l = speed * -25
        r = speed * -50
        m = 'br' + str(speed)
        move_robot(l, r, 1, m)
    return

def change_direction(key):
    direction = CONST_STOP
    if key in ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']:
        if key == 'q':
            direction = CONST_FORWARD_LEFT
        elif key == 'w':
            direction = CONST_FORWARD
        elif key == 'e':
            direction = CONST_FORWARD_RIGHT
        elif key == 'a':
            direction = CONST_ROTATE_LEFT
        elif key == 's':
            direction = CONST_STOP
        elif key == 'd':
            direction = CONST_ROTATE_RIGHT
        elif key == 'z':
            direction = CONST_BACK_LEFT
        elif key == 'x':
            direction = CONST_BACK
        elif key == 'c':
            direction = CONST_BACK_RIGHT
    return direction

if __name__ == "__main__":
    # Create a Create2 Bot
    port = '/dev/ttyUSB0'  # this is the serial port on my raspberry pi
    baud = {
        'default': 115200,
        'alt': 19200  # shouldn't need this unless you accidentally set it to this
    }

    bot = pycreate2.Create2(port=port, baud=baud['default'])
    bot.start()
    bot.safe()

    print('Remote Control Roomba')
    print('---------------------')
    print('Move Roomba with the following keys:')
    print('     q w e')
    print('     a s d')
    print('     z x c')
    print('Accelerate and decelerate with the following keys:')
    print('     o')
    print('     l')
    print('Exit the program with key:')
    print('     p')

    done = False
    key = 's'
    direction = CONST_STOP
    speed = 1
    while not done:
        key = getkey()
        if key in ['o', 'l']:
            speed = calc_speed(key, speed)
            turn_robot(direction, speed)
        elif key in ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']:
            direction = change_direction(key)
            turn_robot(direction, speed)
        elif key == 'p':
            turn_robot(CONST_STOP, 0)
            done = True

    print('shutting down ... bye')
    bot.drive_stop()
    time.sleep(0.1)
