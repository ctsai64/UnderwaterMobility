#last update 1/25/2023

# Servo Control

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servoPins = [27, 22, 23, 24]
for p in servoPins:
    GPIO.setup(p, GPIO.OUT)
north = GPIO.PWM(servoPins[0], 50)
south = GPIO.PWM(servoPins[1], 50)
east = GPIO.PWM(servoPins[2], 50)
west = GPIO.PWM(servoPins[3], 50)

north.start(0)
south.start(0)
west.start(0)
east.start(0)

def servoGo(servo,dutyCycle,ti):
    servo.start(int(dutyCycle))
    time.sleep(int(ti))
    servo.stop()
        
def fillUp(motor):
    motor.start(5)
    time.sleep(30)
    motor.stop()

def warmupSequence():
    servoGo(north)
    servoGo(south)
    servoGo(east)
    servoGo(west)
    
def fillUp(motor):
    motor.start(5)
    time.sleep(30)
    motor.stop()

while(True):
    s = input("Which servo?")
    if(s == "stop"):
        north.stop()
        south.stop()
        west.stop()
        east.stop()
        GPIO.cleanup()
    else:
        d = input("Duty cycle?")
        t = input("Time?")
        if(s == "north"):
            servoGo(north, d, t)
        elif(s == "south"):
            servoGo(south, d, t)
        elif(s == "east"):
            servoGo(east, d, t)
        elif(s == "west"):
            servoGo(west, d, t)

north.stop()
south.stop()
west.stop()
east.stop()

GPIO.cleanup()

# servoPins = [27, 22, 23, 24]
# for p in servoPins:
#    GPIO.setup(p, GPIO.OUT)
#north = GPIO.PWM(servoPins[0], 50)
#south = GPIO.PWM(servoPins[1], 50)
#east = GPIO.PWM(servoPins[2], 50)
#west = GPIO.PWM(servoPins[3], 50)

#north.start(0)
#south.start(0)
#west.start(0)
#east.start(0)

#northFull = False
#southFull = False
#eastFull = False
#westFull = False    

def fillUp(motor):
    motor.start(5)
    time.sleep(30)
    motor.stop()  
    
def emptyDown(motor):
    motor.start(98)
    time.sleep(50)
    motor.stop()

def landing():
    if not northFull: fillUp(north)
    if not southFull: fillUp(south)
    if not eastFull: fillUp(east)
    if not westFull: fillUp(west)

