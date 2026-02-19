import cv2
import numpy as np

width, height = 250, 350
img = cv2.imread('resources/documents.png')

pts1 = np.float32([[340, 3], [607, 59], [150, 335], [470, 459]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

print(img.shape)
cv2.imshow('Image', img)
cv2.imshow('Output', imgOutput)

cv2.imshow('Image', img)

cv2.waitKey(0)