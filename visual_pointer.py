import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Process the image and detect face mesh
    results = face_mesh.process(image_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get the coordinates of the left eye (landmark 33) and right eye (landmark 263)
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]
            h, w, _ = image.shape
            left_eye_x, left_eye_y = int(left_eye.x * w), int(left_eye.y * h)
            right_eye_x, right_eye_y = int(right_eye.x * w), int(right_eye.y * h)

            # Calculate the average position of the eyes
            eye_x = (left_eye_x + right_eye_x) // 2
            eye_y = (left_eye_y + right_eye_y) // 2

            # Move the mouse pointer in the reversed direction
            screen_w, screen_h = pyautogui.size()
            pyautogui.moveTo(eye_x, screen_h - eye_y)

            # Draw face landmarks
            mp_drawing.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

    # Display the image
    cv2.imshow('Eye Tracking', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()