import cv2
import numpy as np
import matplotlib.pyplot as plt

def emptyCircle(event,x,y,flags,params):
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,center=(x,y),radius=40,color=(0,0,255),thickness=5, lineType=cv2.LINE_AA)
    

cv2.namedWindow(winname='image')
cv2.setMouseCallback('image',emptyCircle)

img = cv2.imread('dog_backpack.jpg')

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows