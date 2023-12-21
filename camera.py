import cv2

# Try opening the camera by index
cap = cv2.VideoCapture(0)  # Change the index if needed

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Capture frames or perform other operations
    # ...

# Release the camera when done
cap.release()
