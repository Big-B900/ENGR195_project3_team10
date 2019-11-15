from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.capture('/home/pi/project3/ENGR195_project3_team10/classifier/image.jpg')

