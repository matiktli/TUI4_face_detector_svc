from __future__ import print_function
import requests
import json
import cv2
import sys

addr = ' http://c61b4fd8.ngrok.io'


def testPhotoSend(*argv):
    print('sending')
    test_url = addr + '/addtoqueue'
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    img = cv2.imread(sys.argv[1] + '.jpg')
    _, img_encoded = cv2.imencode('.jpg', img)
    response = requests.post(
        test_url, data=img_encoded.tostring(), headers=headers)
    print(response.content)


testPhotoSend()
