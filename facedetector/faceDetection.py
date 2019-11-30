from ..imports import *


class FaceDetector():

    def __init__(self):
        pass

    def detect_single_face_data(self, path):
        face_data = face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(face_data)[0]
        face_recognition.batch_face_locations()
