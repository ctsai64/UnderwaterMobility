# last updated 2/20/2023

import cv2
import numpy as np

cam = cv2.VideoCapture("/dev/video0")
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

redMin = np.array([0, 70, 50])
redMax = np.array([10, 255, 255])
while (True):
    _,img = cam.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, redMin, redMax)
    red = cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow("Image",img)
    cv2.imshow("Red", red)
    
    for i in range(0, len(mask), 50):
        for n in range(0, len(mask[i]), 50):
            if mask[i][n] == 255:
                print("red")
    if cv2.waitKey(1) == 27:
        cv2.imwrite('img.jpg', img)
        cv2.imwrite('hsv.jpg', hsv)
        cv2.imwrite('mask.jpg', red)
        break

cam.release()
cv2.destroyAllWindows()