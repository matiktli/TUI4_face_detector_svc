from imports import *
import queue


class InMemoryQueue():

    def __init__(self, size=200):
        self.db = queue.PriorityQueue(maxsize=size)


    def putStudentToQueue(self, student_data):
        self.db.put_nowait(student_data)
        pass

    def getStudentFromQueue(self):
        return self.db.get_nowait()

    def viewQueue(self, size):
        data = []
        for i in range(0, max(size, self.db.qsize())):
            data.append(self.db[i])
        return data
