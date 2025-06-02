import os
import cv2
import face_recognition
import pickle

def save_face_image(name, user_id, frame, folder="../known_faces"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{name}_{user_id}.jpg"
    path = os.path.join(folder, filename)
    cv2.imwrite(path, frame)
    return path

def encode_face(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        return encodings[0]
    return None

def update_encodings(name, user_id, encoding, enc_file="../encodings/encodings.pkl"):
    os.makedirs(os.path.dirname(enc_file), exist_ok=True)

    if os.path.exists(enc_file):
        with open(enc_file, "rb") as f:
            data = pickle.load(f)
    else:
        data = {}

    data[user_id] = {
        "name": name,
        "encoding": encoding
    }

    with open(enc_file, "wb") as f:
        pickle.dump(data, f)
