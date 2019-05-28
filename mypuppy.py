import cv2

img = cv2.imread('flipped_fixed_img.jpg')
while True:
    cv2.imshow('Puppy', img)
    
    #Wait at least 1ms and if 'q' is pressed, exit the loop
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
        
cv2.destroyAllWindows()