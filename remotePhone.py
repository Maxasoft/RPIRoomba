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
from bluedot import BlueDot, COLORS
from signal import pause

_speed = 1

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

def robot_forward_left():
    l = _speed * 50
    r = _speed * 25
    m = 'fl' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_forward():
    l = r = _speed * 50
    m = 'f' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_forward_right():
    l = _speed * 25
    r = _speed * 50
    m = 'fr' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_left():
    l = _speed * 50
    r = _speed * -50
    m = 'l' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_stop():
    _speed = 1
    l = 0
    r = 0
    m = 's' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_right():
    l = _speed * -50
    r = _speed * 50
    m = 'r' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_back_left():
    l = _speed * -50
    r = _speed * -25
    m = 'bl' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_back():
    l = _speed * -50
    r = _speed * -50
    m = 'bk' + str(_speed)
    move_robot(l, r, 1, m)
    return

def robot_back_right():
    l = _speed * -25
    r = _speed * -50
    m = 'br' + str(_speed)
    move_robot(l, r, 1, m)
    return

def connect_bluedot():
    print('BlueDot Connected...')
    return

def disconnect_bluedot():
    print('BlueDot Disconnected...')
    raise KeyboardInterrupt
    return

if __name__ == "__main__":
    try:
        # Create a Create2 Bot
        port = '/dev/ttyUSB0'  # this is the serial port on my raspberry pi
        baud = {
            'default': 115200,
            'alt': 19200  # shouldn't need this unless you accidentally set it to this
        }

        bot = pycreate2.Create2(port=port, baud=baud['default'])
        bot.start()
        bot.safe()

        bd = BlueDot(cols=3, rows=3)
        bd.square = True
        bd.border = True
        bd[0, 0].when_pressed = robot_forward_left
        bd[1, 0].color = '00FF00'
        bd[1, 0].when_pressed = robot_forward
        bd[2, 0].when_pressed = robot_forward_right
        bd[0, 1].when_pressed = robot_left
        bd[1, 1].when_pressed = robot_stop
        bd[2, 1].when_pressed = robot_right
        bd[0, 2].when_pressed = robot_back_left
        bd[1, 2].when_pressed = robot_back
        bd[2, 2].when_pressed = robot_back_right

        bd.when_released = robot_stop
        bd.when_client_connects = connect_bluedot
        bd.when_client_disconnects = disconnect_bluedot

        pause()

    except KeyboardInterrupt:
        bot.drive_stop()
        time.sleep(0.1)
    except:
        bot.drive_stop()
        time.sleep(0.1)
