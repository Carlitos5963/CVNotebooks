#This script changes the colors in  quadrants 1, 2, and 4
#The 3rd quadrant will remain the same color as originally read in

import cv2
import numpy as np
import matplotlib.pyplot as plt
        
        
#################################
#### SHOWING IMAGE WITH CV ######
#################################


#Read in the image to be changed
img = cv2.imread('dog_backpack.jpg')

#Used to find the height and width of read in file
img_width = img.shape[0]
img_height = img.shape[1]
print('images width is: ', img_width)
print('\nimages height is: ', img_height)

img_mid = (int(img_width/2), int(img_height/2))
print(img_mid)

#Turns the 1st quadrant red
img[0:img_mid[0],0:img_mid[1],0:2] = 0

#Turns the 2st quadrant green
img[0:img_mid[0],img_mid[1]:img_height,0] = 0
img[0:img_mid[0],img_mid[1]:img_height,2] = 0

#Turns the 4th quadrant blue
img[img_mid[0]:img_width,0:img_mid[1],1:3] = 0


while True:
    cv2.imshow("image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows

