import os
import numpy as np
import cv2
from numpy import asarray
import time

vids = os.listdir()
get = 'mp4 MOV avi'
funcVids = list(filter(lambda a: any([1 if get in a else 0 for get in get.split(' ')]), vids))
#videoLocations = input()


def saveFrames(videos):
    outFile = "frames-"+"-{}-".format(time.localtime())+".npy"
    video = cv2.VideoCapture(videos)
    fps = video.get(cv2.CAP_PROP_FPS)
    success, image = video.read()
    count = 1
    while success:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        data = asarray(gray)
        print(gray)
        success, image = video.read()
        count += 1
    print("1", int(fps), "Total Frames:", count, np.shape(data), "1")
    print(data)
    np.save(outFile, data)


a = map(saveFrames, funcVids)