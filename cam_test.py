# Script for testing the Pi camera
# Author: Chitraaksh
# All Rights Reserved

import cv2

def live_cam():
    # Open the Pi Camera (or USB webcam if connected)
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Could not access the camera.")
        return

    print("Press 'q' to quit the live feed.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Show the live frame
        cv2.imshow("Live Camera Feed", frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    live_cam()
