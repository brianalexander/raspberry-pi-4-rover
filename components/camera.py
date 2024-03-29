from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# Initialize Camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Camera Warming Up
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image=frame.array
    
    cv2.imshow("Frame", image)
    key=cv2.waitKey(1)
    print(key)
    
    rawCapture.truncate(0)
    
    if key == ord("q"):
        break