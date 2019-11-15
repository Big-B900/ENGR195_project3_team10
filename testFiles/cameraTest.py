from picamera import PiCamera
from time import sleep

camera = PiCamera()
sleep(3)
camera.capture('/home/pi/project3/ENGR195_project3_team10/classfier/image.jpg')

