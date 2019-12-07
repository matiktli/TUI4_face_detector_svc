from imports import *
from flask import Flask, request, Response
from facedetector import faceDetection
from db import queue, faces
import base64
from imageio import imread
import io
import sys


app = Flask(__name__)
fd = faceDetection.FaceDetector()
db_queue = queue.InMemoryQueue(3)
db_face = faces.InMemoryFaces()


# If ok it will also add student to queue
@app.route('/addtoqueue', methods=['POST'])
def findFaceOnPhoto():
    image_data = request.data
    b64_bytes = base64.b64encode(image_data)
    b64_string = b64_bytes.decode()
    img = imread(io.BytesIO(base64.b64decode(b64_string)))
    pos, enc = fd.detect_single_face_data(img)
    if pos == None:
        return{'error': 'No face present'}

    match = fd.recognize_face(db_face.faces, enc)
    if match == None:
        return Response(response={'error': 'Could not match face'}, status=404)

    st = student.Student(name=match)  # TODO construct ctudent from match
    # db_queue.putStudentToQueue(st)
    print('This is: ', match)
    return st.toJSON()


@app.route('/removefromqueue', methods=['POST'])
def removeFromQueue():
    student = db_queue.getStudentFromQueue()
    return student.toJSON()


if __name__ == '__main__':

    path = '../face_data_3/'
    if sys.argv[1] == 'true':
        for file in os.listdir(path):
            print('proccessing file: ', file)
            if '.txt' not in file:
                fd.preproccess_video_and_save(path + file)

    app.run()
