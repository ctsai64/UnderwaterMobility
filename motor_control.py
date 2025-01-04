# last updated 1/25/2023

import RPi.GPIO as GPIO
import time

oneA = 17
oneB = 27
oneE = 22
twoA = 23
twoB = 24
twoE = 25

led = 15
servoPin = 18
servo = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(oneA,GPIO.OUT)
GPIO.setup(oneB,GPIO.OUT)
GPIO.setup(oneE,GPIO.OUT)

GPIO.output(oneA,GPIO.LOW)
GPIO.output(oneB,GPIO.LOW)
GPIO.output(oneE,GPIO.LOW)

GPIO.setup(twoA,GPIO.OUT)
GPIO.setup(twoB,GPIO.OUT)
GPIO.setup(twoE,GPIO.OUT)

GPIO.output(twoA,GPIO.LOW)
GPIO.output(twoB,GPIO.LOW)
GPIO.output(twoE,GPIO.LOW)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(servoPin, GPIO.OUT)
servo = GPIO.PWM(servoPin, 50)
servo.start(0)

def left():
    servo.ChangeDutyCycle(1)
    time.sleep(1)
    servo.ChangeDutyCycle(0)
    
def right():
    servo.ChangeDutyCycle(15)
    time.sleep(1)
    servo.ChangeDutyCycle(0)
    
def center():
    servo.ChangeDutyCycle(7.5)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

def spin(t):
    GPIO.output(twoA,GPIO.HIGH)
    GPIO.output(twoB,GPIO.LOW)
    GPIO.output(twoE,GPIO.HIGH)
    time.sleep(t)
    GPIO.output(twoA,GPIO.LOW)
    GPIO.output(twoB,GPIO.LOW)
    GPIO.output(twoE,GPIO.LOW)
    
def empty():
    GPIO.output(oneA,GPIO.HIGH)
    GPIO.output(oneB,GPIO.LOW)
    GPIO.output(oneE,GPIO.HIGH)
    time.sleep(23)
    GPIO.output(oneA,GPIO.LOW)
    GPIO.output(oneB,GPIO.LOW)
    GPIO.output(oneE,GPIO.LOW)
    
def fill():
    GPIO.output(oneA,GPIO.LOW)
    GPIO.output(oneB,GPIO.HIGH)
    GPIO.output(oneE,GPIO.HIGH)
    time.sleep(23)
    GPIO.output(oneA,GPIO.LOW)
    GPIO.output(oneB,GPIO.LOW)
    GPIO.output(oneE,GPIO.LOW)

def letThereBeLight():
    GPIO.output(led, GPIO.HIGH)
    
def clean():
    servo.stop()
    GPIO.cleanup()