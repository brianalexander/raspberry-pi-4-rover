import time

# from track import Track

# # Motor 1 GPIO pin constants
# MOTOR_1_ENABLE = 4
# MOTOR_1_IN1 = 14
# MOTOR_1_IN2 = 15

# # Motor 2 GPIO pin constants
# MOTOR_2_ENABLE = 17
# MOTOR_2_IN1 = 18
# MOTOR_2_IN2 = 27


class Base:
    def __init__(self, left_track, right_track):
        self.left_track = left_track
        self.right_track = right_track

    def __del__(self):
        pass

    def stop(self, ):
        self.left_track.disable()
        self.right_track.disable()

    def forward(self, ):
        self.left_track.forward()
        self.right_track.forward()

    def reverse(self, ):
        self.left_track.reverse()
        self.right_track.reverse()

    def rotate_cw(self, ):
        self.left_track.forward()
        self.right_track.reverse()

    def rotate_ccw(self, ):
        self.left_track.reverse()
        self.right_track.forward()


if __name__ == "__main__":
    left_track = Track(4, 14, 15)
    right_track = Track(7, 18, 27)

    base = Base(left_track, right_track)
    base.forward()
    time.sleep(2)
    base.reverse()
    time.sleep(2)
    base.rotate_cw()
    time.sleep(2)
    base.rotate_ccw()
    time.sleep(2)
