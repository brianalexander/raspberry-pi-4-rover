from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio

import time
import atexit


# Create a simple PCA9685 class instance.
i2c = busio.I2C(SCL, SDA)


pca = PCA9685(i2c)
pca.frequency = 50


class Servo:
    def __init__(self, channel, initial_angle=180, min_pulse=1000, max_pulse=2000):
        self.servo = servo.Servo(
            pca.channels[channel], min_pulse=min_pulse, max_pulse=max_pulse)
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.angle = initial_angle

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        if(angle > 180 or angle < 0):
            return
        self.servo.angle = angle
        self._angle = angle

    def dec_angle(self):
        try:
            self.angle = int(self.angle - 1)
        except ValueError:
            print("ERROR: Angle out of range ", self.angle)

    def inc_angle(self):
        try:
            self.angle = int(self.angle + 1)
        except ValueError:
            print("ERROR: Angle out of range ", self.angle)

    def move_to(self, angle):
        self.angle = angle


def get_servo(channel):
    duty
    return pca.channels[channel]


def cleanup_servo(sig=None, frame=None):
    print("cleaning up servos...")
    pca.deinit()


atexit.register(cleanup_servo)

if __name__ == "__main__":
    # sensor_block
    servo11 = Servo(11, min_pulse=950, max_pulse=1600, initial_angle=180)

    # shoulder
    servo12 = Servo(12, initial_angle=90, min_pulse=600, max_pulse=2500)
    # elbow
    servo13 = Servo(13, initial_angle=130, min_pulse=600, max_pulse=2200)
    # wrist
    servo14 = Servo(14, initial_angle=90, min_pulse=600, max_pulse=2500)
    # gripper
    servo15 = Servo(15, initial_angle=90, min_pulse=600, max_pulse=1400)
