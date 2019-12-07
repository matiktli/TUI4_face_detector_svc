from imports import *


class InMemoryFaces():

    def __init__(self, pathToFiles='../face_data_3'):
        self.faces = []
        for file in os.listdir(pathToFiles):
            if '.txt' in file:
                data = self.__extractDataFromFile(pathToFiles + '/' + file)
                data = self.__convert_data(data, file)
                self.faces.append(data)

    def __extractDataFromFile(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
            return data

    def __convert_data(self, file_data, file_name):
        result = {}
        result['name'] = file_name[:-8]

        enc_of_person = []
        for frame_no in file_data:
            frame = file_data[frame_no]
            enc = frame[0]['enc']
            enc_of_person.append(enc)

        result['encs'] = enc_of_person
        return result

    def getKnownEncodings(self):
        def getEnc(data):
            return data['enc']
        return map(getEnc, self.faces)
