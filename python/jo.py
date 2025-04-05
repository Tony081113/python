import cv2
import numpy as np
img=cv2.imread('5f18f69ffdcbfa2418b266d44f9ec47d.jpg')
print(img.shape)
img[:,:,2]=200
cv2.imshow('out',img)
cv2.waitKey(0)
cv2.destroyALLWindows()
