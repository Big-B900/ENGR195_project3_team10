import time
from adafruit_crickit import crickit

def rotateThetrough(t):

    if t == 1:
        print("Your object is going into the trash bin")
        crickit.servo_1.angle = 90
        time.sleep(1)
        crickit.servo_1.angle = 0
        time.sleep(5)
        crickit.servo_1.angle = 9
        print("Common trash items: food, styrofoam, soiled materials, electrical cords")
        time.sleep(5)
    else:
        print("Your object is going into recycling")
        crickit.servo_1.angle = 90
        time.sleep(1)
        crickit.servo_1.angle = 180
        time.sleep(5)
        crickit.servo_1.angle = 90
        print("Common recyclables: plastic water bottles, grocery bags, glass containers")
        time.sleep(5)

def funFacts(y):
    facts = ["According to the EPA, 75% of American waste is recyclable, and 30% of it is actually recycled\n","Americans throw away about 28 billion bowls and jars every year\n","A glass container can go from a recycling bin to s tore shelf in as few as 30 days\n","The average person generates over 4 pounds of trash each day\n"]

    print(facts[y%4])

ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1
ss.pin_mode(BUTTON_1,ss.INPUT_PULLUP)
print("Insert your object")
i = 0

while True:
        if not(ss.digital_read(BUTTON_1)):
            rotateThetrough(1)
        i += 1
        if(i%1000 == 0):
            funFacts(int(i / 1000))

