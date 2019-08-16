from components.track import Track
from components.servo import Servo
from components.depth_sensor import DepthSensor


from units.sensor_block import SensorBlock
from units.base import Base

#
# Setup components
#
left_track = Track(4, 14, 15)
right_track = Track(17, 18, 27)
servo11 = Servo(11, min_pulse=950, max_pulse=1600, initial_angle=180)
depth_sensor = DepthSensor(11, 8)

#
# Compose Units
#
sensor_block = SensorBlock(servo11, depth_sensor)
base = Base(left_track, right_track)

import sys, termios, tty, os, time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def memoize(f):
    last_pressed = [None]
    def helper(x):
        if x == last_pressed[0]:
            print("key didn't change")
            return
        print('updating action')
        last_pressed[0] = x            
        f(x)
    return helper

def switch(key):
    switcher = {
        'q': base.rotate_ccw,
        'e': base.rotate_cw,
        'w': base.forward,
        's': base.reverse,
        'z': base.stop,
        'f': sensor_block.tilt_up,
        'r': sensor_block.tilt_down,
    }

    switcher.get(key)()


while(True):
    key = getch()

    switch(key)
