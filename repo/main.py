import numpy as np
import cv2
from numpy import asarray

outFile = "frames.npy"
videoLocations = input()

def saveFrames(videos):
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
    print("1", int(fps), "Total Frames:", count,np.shape(data),"1")
    print(data)
    np.save(outFile, data)


saveFrames(videoLocations)
