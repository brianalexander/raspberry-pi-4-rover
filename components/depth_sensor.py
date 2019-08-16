import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# trigger = 11
# echo = 8


class DepthSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin

        GPIO.setup(self.trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.echo, GPIO.IN)

    def __del__(self):
        GPIO.cleanup([self.trig, self.echo])

    def getDistance(self):
        GPIO.output(self.trig, GPIO.LOW)

        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig, GPIO.LOW)

        # Set start time
        while not GPIO.input(self.echo):
            pass
        ping = time.time()

        # Set finish time
        while GPIO.input(self.echo):
            pass
        pong = time.time()

        return (pong-ping)*34300/2


if __name__ == "__main__":
    sensor = DepthSensor(11, 8)
    for _ in range(10):
        print(sensor.getDistance())
        time.sleep(1)
