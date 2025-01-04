#last updated 2/19/2023

import RPi.GPIO as GPIO
import time
    
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
    
def clean():
    GPIO.cleanup()

light()

while True:
    print("Enter Command(l for list): ")
    key = input()
    if key == "1":
        one()
    elif key == "2":
        two()
    elif key == "0":
        light()
    elif key == "f":
        fill()
    elif key == "e":
        empty()
    elif key == "c":
        clean()
    elif key == "s":
        off()
    elif key == "l":
        print("0 = light")
        print("1 = motor one")
        print("2 = motor two")
        print("e = empty")
        print("f = fill")
        print("c = clean")

