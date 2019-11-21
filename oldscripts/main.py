from adafruit_crickit import crickit
import functions.py as fn


ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1
ss.pin_mode(BUTTON_1,ss.INPUT_PULLUP)

while True:
    if not(ss.digital_read(BUTTON_1)):
        print("yuh")
        fn.rotateThetrough(1)
