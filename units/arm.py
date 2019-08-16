import time
from servo import get_servo

if __name__ == "__main__":
    servo12 = get_servo(12, 180)
    servo13 = get_servo(13, 90)
    servo14 = get_servo(14, 180)
    servo15 = get_servo(15, 90)

    servo12.angle = 0
    servo13.angle = 20
    servo14.angle = 90
    servo15.angle = 10

    time.sleep(1)
