import cv2
# Function to handle mouse events
def click_event(event, x, y, flags, params):
    # Checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'({x}, {y})')
        # Put coordinates as text on the image
        cv2.putText(img, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow('Image Coordinates', img)

# Read the input image
img = cv2.imread('resources/documents.png') 

# Check if image loaded successfully
if img is None:
    print("Error: Could not read image file. Check the path.")
else:
    # Create a window and bind the callback function to it
    cv2.namedWindow('Image Coordinates')
    cv2.setMouseCallback('Image Coordinates', click_event)

    print("Click on the image window to get coordinates. Press 'Esc' to exit.")

    # Display the image and wait for a key press
    while True:
        cv2.imshow('Image Coordinates', img)
        # Wait for a key press and exit if 'Esc' (27) is pressed
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    # Close all windows
    cv2.destroyAllWindows()