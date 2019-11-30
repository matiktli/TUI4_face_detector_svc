from imports import *
from PIL import Image, ImageDraw


class ProcUtil():

    def __init__(self):
        pass

    def detect_face_from_data(self, image_data):
        face_locations = face_recognition.face_locations(image_data)
        if not face_locations:
            return None, None

        top, right, bottom, left = self.__findMainFace(face_locations)
        face_encoding = face_recognition.face_encodings(
            image_data, [face_locations[0]])[0]

        return (top, right, bottom, left), face_encoding

    def detect_face_from_path(self, path):
        face_img = face_recognition.load_image_file(path)
        return self.detect_face_from_data(face_img)

    def __findMainFace(self, faces_locations):
        return faces_locations[0]
        # for top, right, bottom, left in faces_locations

    def detect_faces_on_video_and_create_metadata(self, path, scale=400, numPhotos=20):
        data = []
        print('File: ', path)
        vid = cv2.VideoCapture(path)
        frameCounter = 0
        while (frameCounter < 300 and len(data) < numPhotos):
            ret, frame = vid.read()
            frameCounter +=1
            if frameCounter % 10 == 0 and ret == True:
                frame = frame[:, :, ::-1]
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                height, width, depth = frame.shape
                imgScale = scale/height
                newX,newY = frame.shape[1]*imgScale, frame.shape[0]*imgScale
                frame = cv2.resize(frame,(int(newX),int(newY)))
                pos, enc = self.detect_face_from_data(frame)
                print('{} --> {}.'.format(frameCounter, pos))
                data.append([pos, enc])
                if pos:
                    cv2.rectangle(frame, (pos[1], pos[0]), (pos[3], pos[2]), (255,0,0), 2)
                cv2.imshow('frame', frame)
            if cv2.waitKey(1)  & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        vid.release()
        return data
