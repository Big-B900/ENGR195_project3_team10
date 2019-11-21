import time
from adafruit_crickit import crickit

def rotateThetrough(t):

    if t == 1:
        crickit.servo_1.angle = 90
        time.sleep(1)
        crickit.servo_1.angle = 0
        time.sleep(5)
        crickit.servo_1.angle = 90
    else:
        crickit.servo_1.angle = 90
        time.sleep(1)
        crickit.servo_1.angle = 180
        time.sleep(5)

        crickit.servo_1.angle = 90

ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1
ss.pin_mode(BUTTON_1,ss.INPUT_PULLUP)

while True:
    if not(ss.digital_read(BUTTON_1)):
        print("yuh")
        rotateThetrough(1)