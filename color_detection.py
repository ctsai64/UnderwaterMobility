# last update 2/18/2023

import cv2
import numpy as np

testImg = cv2.imread("red.jpg")

# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture("/dev/video0")
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

# define range of HSV value for red
#redMin = np.array([0, 70, 50], np.uint8)
#redMax = np.array([10, 255, 255], np.uint8)

# define BGR values for red
redMin = np.array([17, 50, 100], np.uint8)
redMax = np.array([50, 56, 200], np.uint8)

found = False;

def findRed(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, redMin, redMax)
    print(mask)
    for r in mask:
        for c in r:
            print(c)
            if c == 255:
                return True
            else:
                return False

while True:
    _, img = cam.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, redMin, redMax)
    cv2.imshow("Mask", mask)
    cv2.imshow("HSV", hsv)
    if cv2.waitKey(1) == 27:
        break
    found = findRed(img)

cam.release()
cv2.destroyAllWindows()


def bullsEye(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, redMin, redMax)
    for r in range(mask.shape[0]/3, mask.shape[0]/3*2):
        for c in range(mask.shape[1]/3, mask.shape[1]/3*2):
            print(c)
            if c == 255:
                return True
            else:
                return False

def chargingBull():
    success, img = cam.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, redMin, redMax)
    cv2.waitKey(0)
    cam.release()
    for r in mask:
        for c in r:
            print(c)
            if c == 255:
                return True
            else:
                return False
    #found = []
    # for r in range(0, 480, 10):
    #    for c in range(0, 640, 10):
    #        print(mask[r][c])
    #        if mask[r][c] == 255:
    #            found.append([r,c])  
    # print(found)
    
            
#while True:
#    success, img = cam.read()

    # convert to HSV image
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # isolate color in image
    # mask = cv2.inRange(hsv, redMin, redMax)

    # simplyfy image
    # plain = np.ones((5, 5), "uint8")
    # rmask = cv2.dilate(rmask, plain)
    #red = cv2.bitwise_and(img, img, mask = rmask)
    
    # track color
    # cont, hier, _ = cv2.findContours(rmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # return location
    #for p, c in enumerate(cont):
    #    area = cv2.contourArea(c)
    #    if(area > 300):
    #        x, y, w, h = cv2.boundingRect(c)
    #        print(x, y, w, h)

    #cv2.imshow('image', mask)

    #if cv2.waitKey(1) == 27:
    #    break

#cam.release()
#cv2.destroyAllWindows()
