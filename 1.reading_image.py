import cv2

## Read and display an image

# img = cv2.imread('resources/cat.jpg')
# cv2.imshow('Cat', img)
# cv2.waitKey(0)  # Wait until a key is pressed

## Read and display a video
# cap = cv2.VideoCapture('resources/vid1.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow('output', img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

## Read and display from webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)  # Set height

while True:
    success, img = cap.read()
    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break