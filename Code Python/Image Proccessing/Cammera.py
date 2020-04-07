import numpy as np
import cv2

cap = cv2.VideoCapture(2)
x = 0
y = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    Canny = cv2.Canny(gray,100,150)
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    frame = cv2.drawContours(frame, contours, -1, (0,255,0), 1)
    x = 0
    y = 0
    cont = contours[0]
    for i in range(len(cont)):
        x += cont[0][0][0]
        y += cont[0][0][1]
    frame = cv2.circle(frame,(x/len(cont),y/len(cont)), 5, (0,0,255), -1)


    cv2.imshow('threshold',thresh)
    cv2.imshow('Canny',Canny)
    cv2.imshow('frame',frame )


    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(contours)
        break

cap.release()
cv2.destroyAllWindows()
