import cv2
import face_recognition
import pickle
import os
import pyttsx3
import csv
from datetime import datetime

ENCODINGS_PATH = "../encodings/encodings.pkl"
CSV_FILE = "attendance.csv"

def load_encodings():
    if os.path.exists(ENCODINGS_PATH):
        with open(ENCODINGS_PATH, "rb") as f:
            return pickle.load(f)
    return {}

def save_attendance_to_csv(attendance_list):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header if file is new
        if not file_exists:
            writer.writerow(["User ID", "Name", "Timestamp"])
        for record in attendance_list:
            writer.writerow(record)

def recognize_and_mark():
    data = load_encodings()
    if not data:
        print("[ERROR] No encodings found.")
        return

    known_encodings = []
    user_ids = []
    names = []

    for user_id, info in data.items():
        known_encodings.append(info['encoding'])
        user_ids.append(user_id)
        names.append(info['name'])

    cap = cv2.VideoCapture(0)
    marked_users = set()
    attendance_list = []

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speaking speed

    print("[INFO] Press 'q' to quit attendance session.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        for face_encoding, face_location in zip(encodings, faces):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            distances = face_recognition.face_distance(known_encodings, face_encoding)

            name = "Unknown"

            if True in matches:
                best_match_index = distances.argmin()
                if matches[best_match_index]:
                    user_id = user_ids[best_match_index]
                    name = names[best_match_index]

                    if user_id not in marked_users:
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        marked_users.add(user_id)
                        attendance_list.append([user_id, name, timestamp])
                        print(f"[INFO] Attendance marked for {name} ({user_id}) at {timestamp}")

                        # Voice greeting
                        engine.say(f"Welcome {name}. Your attendance is marked.")
                        engine.runAndWait()

            # Draw box and name on the frame
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 2)

        cv2.imshow("Face Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if attendance_list:
        save_attendance_to_csv(attendance_list)
        print(f"[INFO] Attendance saved to {CSV_FILE}")
    else:
        print("[INFO] No attendance marked this session.")

if __name__ == "__main__":
    recognize_and_mark()
