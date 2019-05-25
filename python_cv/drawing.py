import numpy as np
import cv2

print ("DRAWING OPENCV PYTHON")

img = np.zeros ((512,512,3), np.uint8)

print(img)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),500)
cv2.imshow("img", img)



cv2.waitKey(0)
cv2.destroyAllWindows()