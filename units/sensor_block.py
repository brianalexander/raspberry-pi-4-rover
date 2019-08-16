import time

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from components.depth_sensor import DepthSensor
from components.servo import Servo


class SensorBlock:
    def __init__(self, servo, ultrasonic):
        self.servo = servo
        self.ultrasonic = ultrasonic
        pass

    def __del__(self, ):
        pass

    def move(self, theta):
        self.servo.move_to(theta)

    def tilt_down(self):
        self.servo.inc_angle()

    def tilt_up(self):
        self.servo.dec_angle()


if __name__ == "__main__":
    servo11 = Servo(11, min_pulse=950, max_pulse=1600, initial_angle=180)
    depth_sensor = DepthSensor(11, 8)
    sensor_block = SensorBlock(servo11, depth_sensor)

    while(True):
        key = input()
        if (key == 'w'):
            sensor_block.tilt_up()
        else:
            sensor_block.tilt_down()
