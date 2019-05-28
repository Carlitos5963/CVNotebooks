import cv2
import numpy as np

#VARIABLES

#True while mouseButtonDown, false when up
drawing = False
ix, iy = -1, -1

#FUNCTION
def draw_rectangle(event,x,y,flags,params):
    
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
      
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,pt1=(ix,iy), pt2=(x,y),color=(0,255,0), thickness=-1, lineType=cv2.LINE_AA)

    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,pt1=(ix,iy), pt2=(x,y),color=(0,255,0), thickness=-1, lineType=cv2.LINE_AA)

#SHOWING THE IMAGE

#BLACK IMAGE
img = np.zeros(shape=(720,720,3),dtype=np.int8)

cv2.namedWindow(winname='image')
cv2.setMouseCallback('image', draw_rectangle)

while True:
    cv2.imshow('image', img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
        
cv2.destroyAllWindows