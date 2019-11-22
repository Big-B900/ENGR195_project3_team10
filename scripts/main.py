from adafruit_crickit import crickit
import functions as fn
from picamera import PiCamera
from fabric import task, Connection
import time
from ast import literal_eval
#from kanga2:.pythonTest import testfn

ss = crickit.seesaw
BUTTON_1 = crickit.SIGNAL1
ss.pin_mode(BUTTON_1,ss.INPUT_PULLUP)
camera = PiCamera()
c = Connection('kanga2')
direction = 0

#materials
paper = 0.0
cardboard = 0.0
plastic = 0.0
metal = 0.0
glass = 0.0

#thresholds
allThreshold = .4



i=0
funFactsTime = 1000
while True:
    if not(ss.digital_read(BUTTON_1)):
        print("yuh")
        fn.picToTop(camera)
        #testfn()
        #make sure picture is recieved
        time.sleep(.5)
        #this runs the neural network on the laptop and returns a dictionary of the confidences
        result = fn.vision(c)
        
        #need a function to parse it (nevermind python does it for me )
        #example output: {'paper': 0.45938486, 'cardboard': 0.42542723, 'plastic': 0.06604799, 'metal': 0.036904056, 'glass': 0.012235973}
        parsedResult = literal_eval(result)
        
        paper = parsedResult['paper']
        cardboard = parsedResult['cardboard']
        plastic = parsedResult['plastic']
        metal = parsedResult['metal']
        glass = parsedResult['glass']
		
        
        print(result)
       
        #logic
        if paper < allThreshold and cardboard < allThreshold and plastic < allThreshold and metal < allThreshold and glass < allThreshold:
            direction = 1
        else:
            direction = 0
        
        
        fn.rotateThetrough(direction)
   
    #print(i)
    if(i%funFactsTime == 1):
           fn.funFacts(int(i / funFactsTime))
    i += 1
