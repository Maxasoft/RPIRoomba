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

class BlueDotRobot:

    _bot = None
    _bd = None
    _speed = 1

    def robot_move(self, lft, rht, dt, s):
        print(s)
        self._bot.digit_led_ascii(s)
        self._bot.drive_direct(lft, rht)
        time.sleep(dt)
        return

    def robot_accelerate(self):
        if self._speed < 10:
            self._speed = self._speed + 1
        return

    def robot_decelerate(self):
        if self._speed > 1:
            self._speed = self._speed - 1
        return

    def robot_forward_left(self):
        l = self._speed * 50
        r = self._speed * 25
        m = 'fl' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_forward(self):
        l = r = self._speed * 50
        m = 'f' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_forward_right(self):
        l = self._speed * 25
        r = self._speed * 50
        m = 'fr' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_left(self):
        l = self._speed * 50
        r = self._speed * -50
        m = 'l' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_stop(self):
        self._speed = 1
        l = 0
        r = 0
        m = 's' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_right(self):
        l = self._speed * -50
        r = self._speed * 50
        m = 'r' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_back_left(self):
        l = self._speed * -50
        r = self._speed * -25
        m = 'bl' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_back(self):
        l = self._speed * -50
        r = self._speed * -50
        m = 'bk' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_back_right(self):
        l = self._speed * -25
        r = self._speed * -50
        m = 'br' + str(self._speed)
        self.robot_move(l, r, 1, m)
        return

    def robot_exit(self):
        self._bot.drive_stop()
        raise KeyboardInterrupt
        return

    def connect_bluedot(self):
        print('BlueDot Connected...')
        return

    def disconnect_bluedot(self):
        print('BlueDot Disconnected...')
        return
    
    def main(self):
        try:
            # Create a Create2 Bot
            port = '/dev/ttyUSB0'  # this is the serial port on my raspberry pi
            baud = {
                'default': 115200,
                'alt': 19200  # shouldn't need this unless you accidentally set it to this
            }

            self._bot = pycreate2.Create2(port=port, baud=baud['default'])
            self._bot.start()
            self._bot.safe()

            self._bd = BlueDot(cols=4, rows=3)
            self._bd.square = True
            self._bd.border = True
            self._bd[0, 0].when_pressed = self.robot_forward_left
            self._bd[1, 0].when_pressed = self.robot_forward
            self._bd[2, 0].when_pressed = self.robot_forward_right
            self._bd[3, 0].when_pressed = self.robot_accelerate
            self._bd[0, 1].when_pressed = self.robot_left
            self._bd[1, 1].when_pressed = self.robot_exit
            self._bd[2, 1].when_pressed = self.robot_right
            self._bd[3, 1].when_pressed = self.robot_exit
            self._bd[0, 2].when_pressed = self.robot_back_left
            self._bd[1, 2].when_pressed = self.robot_back
            self._bd[2, 2].when_pressed = self.robot_back_right
            self._bd[3, 2].when_pressed = self.robot_decelerate

            self._bd.when_released = self.robot_stop
            self._bd.when_client_connects = self.connect_bluedot
            self._bd.when_client_disconnects = self.disconnect_bluedot

            pause()

        except KeyboardInterrupt:
            self._speed = 0
        except:
            self._speed = 0
        return

def main():
    bd_robot = BlueDotRobot()
    bd_robot.main()
    return

if __name__ == "__main__":
    main()
