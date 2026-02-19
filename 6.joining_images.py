import cv2
import numpy as np

img = cv2.imread('resources/hand.jpg')
img_resized = cv2.resize(img, (450, 300))

imgHor = np.hstack((img_resized, img_resized))
imgVer = np.vstack((img_resized, img_resized))

print(img_resized.shape)
cv2.imshow('Horizontal', imgHor)
cv2.imshow('Vertical', imgVer)
cv2.waitKey(0)
