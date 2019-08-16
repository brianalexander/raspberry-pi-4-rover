import time
import RPi.GPIO as GPIO
from functools import wraps

GPIO.setmode(GPIO.BCM)


class Track:
    def __init__(self, enable_pin, pin1, pin2):
        self.enable_pin = enable_pin
        self.pin1 = pin1
        self.pin2 = pin2

        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        self.disable()

    def __del__(self):
        self.disable()
        GPIO.cleanup([self.enable_pin, self.pin1, self.pin2])

    def _enable_disable_dec(func):
        @wraps(func)
        def wrapper(*args):
            args[0].disable()
            func(args[0])
            args[0].enable()

        return wrapper

    def disable(self, ):
        print('disabling')
        GPIO.output(self.enable_pin, GPIO.LOW)

    def enable(self, ):
        print('enabling')
        GPIO.output(self.enable_pin, GPIO.HIGH)

    @_enable_disable_dec
    def forward(self, ):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    @_enable_disable_dec
    def reverse(self, ):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)


if __name__ == "__main__":
    left_track = Track(4, 14, 15)
    right_track = Track(17, 18, 27)

    left_track.forward()
    right_track.forward()
    time.sleep(5)
