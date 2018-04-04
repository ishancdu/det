import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if (cap.isOpened()== False):
    print("Error opening video stream or file")

#while(True):
while(cap.isOpened()):
    
    ret, image = cap.read()
    cv2.imshow("image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
cap.release()
cv2.destroyAllWindows()
