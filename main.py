#Author: Chitraaksh
# All Rights Reserved

import cv2
import face_recognition
import pickle
import os
import time

DATA_FILE = "faces.dat"

def enroll_face():
    cam = cv2.VideoCapture(0)
    print("Look at the camera... capturing will start in 10 seconds.")
    time.sleep(10)   # wait before capture

    ret, frame = cam.read()
    cam.release()

    if not ret:
        print("Failed to capture image.")
        return

    # Show the captured frame for 3 seconds
    cv2.imshow("Captured Face", frame)
    cv2.waitKey(3000)  # 3000 ms = 3 seconds
    cv2.destroyAllWindows()

    # Process and save encoding
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    if face_encodings:
        with open(DATA_FILE, "wb") as f:
            pickle.dump(face_encodings, f)
        print("Face enrolled successfully!")
    else:
        print("No face detected. Try again.")

def recognize_faces():
    with open(DATA_FILE, "rb") as f:
        known_faces = pickle.load(f)

    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            if True in matches:
                # Draw rectangle around known face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        enroll_face()
    else:
        recognize_faces()
