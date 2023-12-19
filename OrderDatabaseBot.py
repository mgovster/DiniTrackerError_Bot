from turtle import goto
#from xmlrpc.client import DateTime
import pyautogui as py
import time
import winsound
from datetime import datetime

#this program is to help find error 500 in order database
#have website and dev tools open in monitor 1 (if switching to different monitors, re-save the images to have the correct resolution of the monitor)

ordernumberBoxLoc = (0,0)

pdClick = r'images/DoClickWithArrow.png'
searchOrderNo = r'images/OrderNumberBox.png'
py.FAILSAFE=True


def setUpControls():
    time.sleep(3)
    #set up spots
    ordernumberBoxLoc = py.locateOnScreen(pdClick, confidence=.1)
    #end set ups
    
    #winsound.Beep(500,500)
    time.sleep(1)


OrderNoloc = py.locateOnScreen(searchOrderNo,confidence=.7)
loc3 = py.locateOnScreen(pdClick,confidence=.7)
#.7 seems fine for now
setUpControls()

def goToOrderBox(daOrderNo):
    #barely hits corner
    py.moveTo(OrderNoloc[0]+300,OrderNoloc[1]+10)
    time.sleep(.1)
    
    py.click()
    py.hotkey('ctrl','a')
    #put in orderNo now 
    py.typewrite(daOrderNo,.1)
    py.press('enter')
    print('OrderNo Searched:   ' + daOrderNo)

def checkIfNotFine():
    if (py.locateOnScreen(r'images/uncaughtTypeError.png')):
        return True
    return False

daFile = open('OrderNumberList.txt', 'r') 

print(py.locateOnScreen(py.locateOnScreen(searchOrderNo,confidence=.7)))

while (True):
    line = daFile.readline()
    if not line:
        break
    goToOrderBox(line)
    time.sleep(4)
    if(checkIfNotFine()):   #this will be the check to see if it was fine
        winsound.Beep(3000,500)     #will make a beep sound if run into error
        print('Stopped at OrderNo ' + line)
        thing = datetime.now()
        print(thing)
        while True:
            winsound.Beep(3000,100)
            winsound.Beep(800,100)
            time.sleep(.1)
            break
       
    

print("End Of Program")

