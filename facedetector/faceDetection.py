from .proccessingUtil import ProcUtil
from imports import *


class FaceDetector():

    def __init__(self):
        self.utils = ProcUtil()
        pass

    def detect_single_face_data(self, img_data):
        return self.utils.detect_face_from_data(img_data)

    def recognize_face(self, faces_enc_data, unknown_face):
        known_students_enc = []
        known_student_names = []
        for data in faces_enc_data:
            for enc in data['encs']:
                known_student_names.append(data['name'])
                print('-x-> ', enc)
                known_students_enc.append(enc)

        #known_students_enc = known_students_enc[0]

        matches = face_recognition.compare_faces(
            known_students_enc, unknown_face)
        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(
            known_students_enc, unknown_face)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"
        if matches[best_match_index]:
            name = known_student_names[best_match_index]

        return name

    def preproccess_video_and_save(self, path):
        data = self.utils.detect_faces_on_video_and_return_metadata(path)
        jsonData = {}
        print('Saving: ..')
        with open(path + '.txt', 'w') as outfile:
            for i, (pos, enc) in enumerate(data):
                jsonData[str(i)] = []
                jsonData[str(i)].append({
                    'pos': [p for p in pos],
                    'enc': enc.tolist()
                })
            json.dump(jsonData, outfile)
