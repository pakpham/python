import cv2
import numpy as np
from matplotlib import pyplot as plt

print("PAK")
# Load an color image in grayscale
img1 = cv2.imread('pic1.jpg',1)
img2 = cv2.imread('pic2.png',0)
#print(img)
# cv2.imshow('image', img2)
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
# elif key == ord('s'):
#     cv2.imwrite('messigray.png', img2)
#     cv2.destroyAllWindows()


plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
cv2.destroyAllWindows()

