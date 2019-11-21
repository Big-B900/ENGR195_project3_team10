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

while True:
    if not(ss.digital_read(BUTTON_1)):
        #print("yuh")
        fn.picToTop(camera)
        #testfn()
        time.sleep(.5)
        result = fn.vision(c)
        print(result.stdout.strip())
        fn.rotateThetrough(1)
