import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = (255, 0, 0)

## create a line
cv2.line(img, (0, 0), (256, 256), (0, 255, 0), thickness=3)
cv2.line(img, (256, 256), (0, img.shape[0]), (0, 255, 0), thickness=3)
cv2.line(img, (256, 256), (img.shape[1], img.shape[0]), (0, 255, 0), thickness=3)
cv2.line(img, (256, 256), (img.shape[1], 0), (0, 255, 0), thickness=3)
cv2.line(img, (256-50, 256-50), (256+50, 256-50), (0, 0, 255), thickness=5)
cv2.line(img, (256-50, 256-50), (256-50, 256+50), (0, 0, 255), thickness=5)
cv2.line(img, (256+50, 256-50), (256+50, 256+50), (0, 0, 255), thickness=5)
cv2.line(img, (256-50, 256+50), (256+50, 256+50), (0, 0, 255), thickness=5)

# create a rectangle
cv2.rectangle(img, (0, 0), (200, img.shape[0]), (255, 255, 0), thickness=3)
cv2.rectangle(img, (img.shape[0]-200, 0), (img.shape[0], img.shape[0]), (255, 255, 0), thickness=3)

# create a circle
cv2.circle(img, (256, 256), 100, (0, 255, 255), thickness=3)

# create a text
cv2.putText(img, 'Hazel', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), thickness=3)

cv2.imshow('Shapes and Text', img)
cv2.waitKey(0)