from adafruit_crickit import crickit
import functions as fn
from picamera import PiCamera
from fabric import task, Connection
import time
#from kanga2:.pythonTest import testfn

ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1
ss.pin_mode(BUTTON_1,ss.INPUT_PULLUP)
camera = PiCamera()
c = Connection('kanga2')
direction = 0

while True:
    if not(ss.digital_read(BUTTON_1)):
        #print("yuh")
        fn.picToTop(camera)
        #testfn()
        #make sure picture is recieved
        time.sleep(.5)
        #this runs the neural network on the laptop and returns a dictionary of the confidences
        result = fn.vision(c)
        
        print(result)#.stdout.strip())
       
        #logic
        #if result
        
        
        fn.rotateThetrough(direction)
