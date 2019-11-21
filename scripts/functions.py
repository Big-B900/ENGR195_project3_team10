import time
from adafruit_crickit import crickit
import subprocess
from picamera import PiCamera
from fabric import task, Connection

def rotateThetrough(t):

    if t == 1:
        crickit.servo_1.angle = 90
        time.sleep(.1)
        crickit.servo_1.angle = 0
        time.sleep(1)
        crickit.servo_1.angle = 90
        print("your object is going to the landfill")
    else:
        crickit.servo_1.angle = 90
        time.sleep(.1)
        crickit.servo_1.angle = 180
        time.sleep(1)
        crickit.servo_1.angle = 90
        print("your object is being recycled")


def picToTop(camera):

	#take picture
	#camera = PiCamera()
	camera.capture('/home/pi/image.jpg')
	#camera.capture('/home/pi/project3/ENGR195_project3_team10/classifier/image.jpg')
        
	#define where the picture comes from annd goes
	fromPath = '../../../image.jpg'
	toPath = 'kanga2:/home/testuser/gitprojects/ENGR195_project3_team10/classifier/image.jpg'


	#send picture 
	p = subprocess.Popen(["scp",fromPath,toPath], stdout=subprocess.PIPE)
	p.communicate()

def vision(c):
	vision_dir = '/home/testuser/gitprojects/ENGR195_project3_team10/classifier/'
	env_dir = "/home/testuser/"
	result =  c.run("cd {} && source env/bin/activate && cd {} && python3 runvision.py".format(env_dir,vision_dir),hide=True)
	#print(result)



