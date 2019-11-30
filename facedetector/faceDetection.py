from .proccessingUtil import ProcUtil


class FaceDetector():

    def __init__(self):
        self.utils = ProcUtil()
        pass

    def detect_single_face_data(self, path):
        return self.utils.detect_face(path)

    def preproccessVideo(self, path):
        return self.utils.detect_faces_on_video_and_create_metadata(path)
