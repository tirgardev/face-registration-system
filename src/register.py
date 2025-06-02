import cv2
from utils import save_face_image, encode_face, update_encodings

def register_user(name, user_id):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Could not access the camera.")
        return

    print("[INFO] Press 'c' to capture and 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read from camera.")
            break

        cv2.imshow("Register Face - Press 'c' to capture", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Capture
            img_path = save_face_image(name, user_id, frame)
            encoding = encode_face(img_path)
            if encoding is not None:
                update_encodings(name, user_id, encoding)
                print(f"[INFO] {name} registered successfully!")
            else:
                print("[ERROR] No face detected. Try again.")
            break
        elif key == ord('q'):
            print("[INFO] Registration cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    name = input("Enter name: ").strip()
    user_id = input("Enter unique ID: ").strip()
    register_user(name, user_id)
