import cv2
import face_recognition
import pickle
import os

ENCODINGS_PATH = "../encodings/encodings.pkl"

def load_encodings():
    if os.path.exists(ENCODINGS_PATH):
        with open(ENCODINGS_PATH, "rb") as f:
            return pickle.load(f)
    return {}

def recognize_face():
    data = load_encodings()
    if not data:
        print("[ERROR] No encodings found. Register a face first.")
        return

    known_encodings = []
    known_names = []

    for user_id, info in data.items():
        known_encodings.append(info['encoding'])
        known_names.append(f"{info['name']} ({user_id})")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Camera could not be opened.")
        return

    print("[INFO] Press 'q' to quit recognition.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)

            name = "Unknown"

            if matches:
                best_match_index = face_distances.argmin()
                if matches[best_match_index]:
                    name = known_names[best_match_index]

            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        cv2.imshow("Face Recognition - Press 'q' to quit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    recognize_face()
