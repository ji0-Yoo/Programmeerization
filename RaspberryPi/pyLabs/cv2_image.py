import cv2

img = cv2.imread('photo.jpg')

cv2.imshow('photo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()