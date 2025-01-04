# Last updated: 1/3/2025
# Cleaned version

import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

MOTOR_PINS = {
    'one': {'A': 17, 'B': 27, 'E': 22},
    'two': {'A': 23, 'B': 24, 'E': 25},
    'three': {'A': 10, 'B': 9, 'E': 11},
    'four': {'A': 8, 'B': 7, 'E': 1}
}
LED_PIN = 15

GPIO.setmode(GPIO.BCM)
for motor in MOTOR_PINS.values():
    for pin in motor.values():
        GPIO.setup(pin, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

def control_motor(motor, state):
    GPIO.output(MOTOR_PINS[motor]['E'], GPIO.HIGH)
    GPIO.output(MOTOR_PINS[motor]['A'], state)
    GPIO.output(MOTOR_PINS[motor]['B'], not state)

def off():
    for motor in MOTOR_PINS.values():
        for pin in motor.values():
            GPIO.output(pin, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.LOW)

def light(state=True):
    GPIO.output(LED_PIN, state)

SPEED_20ML = 3
SPEED_1M = 1
SPEED_90DEG = 2

RED_MIN = np.array([0, 70, 50])
RED_MAX = np.array([10, 255, 255])

def run():
    cam = cv2.VideoCapture("/dev/video0")
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

    l, s, d = 10, 0, 10
    found = False

    while not found:
        _, img = cam.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, RED_MIN, RED_MAX)
        
        if 255 in mask[::50, ::50]:
            print("Red detected")
            off()
            found = True
        else:
            if d > 0:
                control_motor('one', True)
                control_motor('two', True)
                time.sleep(SPEED_1M)
                off()
                d -= 1
            else:
                control_motor('one', True)
                time.sleep(SPEED_90DEG)
                off()
                s = (s + 1) % 4
                if s == 0:
                    l -= 1
                d = l

    cam.release()
    control_motor('three', False)
    time.sleep(SPEED_20ML)
    off()
    light()

commands = {
    '1': lambda: control_motor('one', True),
    '2': lambda: control_motor('two', True),
    '3': lambda: [control_motor('one', True), control_motor('two', True)],
    '0': light,
    'f': lambda: control_motor('three', False),
    'e': lambda: control_motor('three', True),
    'c': GPIO.cleanup,
    's': off,
    'r': run,
    'l': lambda: print("\n".join([
        "0 = light", "1 = motor one", "2 = motor two", "3 = both motors",
        "e = empty", "f = fill", "s = stop", "r = run", "c = clean", "x = end"
    ]))
}

light()
while True:
    key = input("Enter Command (l for list): ")
    if key == 'x':
        break
    commands.get(key, lambda: None)()

GPIO.cleanup()
