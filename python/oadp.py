import cv2
import numpy as np
img=cv2.imread('5f18f69ffdcbfa2418b266d44f9ec47d.jpg')
B,G,R=cv2.split(img)

zeros=np.zeros(img.shape[:2],dtype=np.uint8)
imgB=cv2.merge([B,zeros,zeros])
imgG=cv2.merge([zeros,G,zeros])
imgR=cv2.merge([zeros,zeros,R])

cv2.imshow('thr',B)
cv2.imshow('sef',G)
cv2.imshow('awd',R)
cv2.waitKey(0)
cv2.destroyAllWindows()
