from adafruit_crickit import crickit
import functions as fn
from picamera import PiCamera
#from kanga2:.pythonTest import testfn

ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1
ss.pin_mode(BUTTON_1,ss.INPUT_PULLUP)
camera = PiCamera()

while True:
    if not(ss.digital_read(BUTTON_1)):
        #print("yuh")
        fn.picToTop(camera)
        #testfn()
        fn.rotateThetrough(1)
