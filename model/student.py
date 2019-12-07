from imports import *


class Student():

    def __init__(self, name='test', subject='test', qualification='test', photoStringData='test'):
        self.name = name
        self.subject = subject
        self.qualification = qualification
        self.photo = photoStringData

    def toJSON(self):
        return {
            'name': self.name,
            'subject': self.subject,
            'qualification': self.qualification,
            'photo': self.photo
        }
