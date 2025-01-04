# last updated 2/20/2023

#UMU IDLDG
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

oneA = 17
oneB = 27
oneE = 22
twoA = 23
twoB = 24
twoE = 25
thrA = 10
thrB = 9
thrE = 11
fouA = 8
fouB = 7
fouE = 1

led = 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(oneA,GPIO.OUT)
GPIO.setup(oneB,GPIO.OUT)
GPIO.setup(oneE,GPIO.OUT)

GPIO.setup(twoA,GPIO.OUT)
GPIO.setup(twoB,GPIO.OUT)
GPIO.setup(twoE,GPIO.OUT)

GPIO.setup(thrA,GPIO.OUT)
GPIO.setup(thrB,GPIO.OUT)
GPIO.setup(thrE,GPIO.OUT)

GPIO.setup(fouA,GPIO.OUT)
GPIO.setup(fouB,GPIO.OUT)
GPIO.setup(fouE,GPIO.OUT)

GPIO.setup(led, GPIO.OUT)

def one():
    GPIO.output(oneE,GPIO.HIGH)
    GPIO.output(oneA,GPIO.HIGH)
    GPIO.output(oneB,GPIO.LOW)

def two():
    GPIO.output(twoE,GPIO.HIGH)
    GPIO.output(twoA,GPIO.HIGH)
    GPIO.output(twoB,GPIO.LOW)

def both():
    GPIO.output(twoE,GPIO.HIGH)
    GPIO.output(twoA,GPIO.HIGH)
    GPIO.output(twoB,GPIO.LOW)
    GPIO.output(oneE,GPIO.HIGH)
    GPIO.output(oneA,GPIO.HIGH)
    GPIO.output(oneB,GPIO.LOW)
    
def off():
    GPIO.output(oneA,GPIO.LOW)
    GPIO.output(oneB,GPIO.LOW)
    GPIO.output(oneE,GPIO.LOW)
    GPIO.output(twoA,GPIO.LOW)
    GPIO.output(twoB,GPIO.LOW)
    GPIO.output(twoE,GPIO.LOW)
    GPIO.output(thrA,GPIO.LOW)
    GPIO.output(thrB,GPIO.LOW)
    GPIO.output(thrE,GPIO.LOW)
    GPIO.output(led, GPIO.LOW)
    
def empty():
    GPIO.output(thrA,GPIO.HIGH)
    GPIO.output(thrB,GPIO.LOW)
    GPIO.output(thrE,GPIO.HIGH)
    
def fill():
    GPIO.output(thrA,GPIO.LOW)
    GPIO.output(thrB,GPIO.HIGH)
    GPIO.output(thrE,GPIO.HIGH)

def light():
    GPIO.output(led, GPIO.HIGH)
    

sp20ml = 3
spdm = 1
sp90d = 2

def run():
    cam = cv2.VideoCapture("/dev/video0")
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

    redMin = np.array([0, 70, 50])
    redMax = np.array([10, 255, 255])
    l = 10
    s = 0
    d = l
    
    found = False
    
    while not found:
        _,img = cam.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, redMin, redMax)
        for i in range(0, len(mask), 50):
            for n in range(0, len(mask[i]), 50):
                if mask[i][n] == 255:
                    print("red")
                    off()
                    found = True 
        if not found:
            if d > 0:
                both()
                time.sleep(spdm)
                off()
                d -= 1
            else:
                if s < 3:
                    one()
                    time.sleep(sp90d)
                    off()
                    s += 1
                else:
                    one()
                    time.sleep(sp90d)
                    off()
                    s = 0
                    l -= 1
                d = l
          
    cam.release()
    fill()
    time.sleep(sp20ml)
    off()
    light()
                       
light()
while True:
    print("Enter Command(l for list): ")
    key = input()
    if key == "1":
        one()
    elif key == "2":
        two()
    elif key == "3":
        both()
    elif key == "0":
        light()
    elif key == "f":
        fill()
    elif key == "e":
        empty()
    elif key == "c":
        GPIO.cleanup()
    elif key == "s":
        off()
    elif key == "r":
        run()
    elif key =="x":
        break
    elif key == "l":
        print("0 = light")
        print("1 = motor one")
        print("2 = motor two")
        print("3 = both motors")
        print("e = empty")
        print("f = fill")
        print("s = stop")
        print("r = run")
        print("c = clean")
        print("x = end")
cam.release()
GPIO.cleanup()