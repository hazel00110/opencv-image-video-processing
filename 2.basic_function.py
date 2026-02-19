import cv2

img = cv2.imread('resources/cat.jpg')

## 1. resize image
img_resized = cv2.resize(img, (640, 480))

## 2. crop image
img_crop = img_resized[100:500, 200:]

## 3. convert to grayscale
img_gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)

## 4. blur image
img_blurred = cv2.GaussianBlur(img_crop, (15, 15), 0)

## 5. edge detection
img_edges = cv2.Canny(img_crop, 200, 200)

print('Image shape:', img.shape)
print('Cropped image shape:', img_crop.shape)
print('Grayscale image shape:', img_gray.shape)
print('Blurred image shape:', img_blurred.shape)
print('Edges image shape:', img_edges.shape)

cv2.imshow('Resized', img_resized)
cv2.imshow('Cropped', img_crop)
cv2.imshow('Grayscale', img_gray)
cv2.imshow('Blurred', img_blurred)
cv2.imshow('Edges', img_edges)
cv2.waitKey(0)
