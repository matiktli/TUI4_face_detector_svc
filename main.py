from facedetector import faceDetection
from imports import *

detector = faceDetection.FaceDetector()



path = '../face_data_3/2.mp4'
data = detector.preproccessVideo(path)

jsonData = {}
print('Saving: ..')
with open(path + '.txt', 'w') as outfile:
    for i, (pos, enc) in enumerate(data):
        jsonData[str(i)] = []
        jsonData[str(i)].append({
            'pos': pos,
            'enc': enc //TODO
        })
    print(jsonData['1'])
    json.dump(jsonData, outfile)
