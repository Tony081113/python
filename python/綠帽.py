import cv2

img = cv2.imread('images.jpg',0)
imga = cv2.cvtColor(img, cv2.IMREAD_COLOR)
cv2.rectangle(imga, (155,5), (216,88), (0,255,0), 3)
cv2.imshow('Tony', imga)
cv2.waitKey(0)
cv2.destroyAllWindows()
