import cv2
import numpy as np

###############
###FUNCTION####
###############

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x,y), radius=50, color=(0,255,0), thickness=-1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, center=(x,y), radius=50, color=(0,0,255), thickness=-1)

cv2.namedWindow(winname='image')

cv2.setMouseCallback('image', draw_circle)

#################################
#### SHOWING IMAGE WITH CV ######
#################################


img = np.zeros(shape=(512,512,3), dtype=np.int8)

while True:
    cv2.imshow('image', img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
        
cv2.destroyAllWindows()