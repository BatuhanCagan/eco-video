import numpy as np
import cv2
from numpy import asarray
from PIL import Image

outFile = "frames.npy"
videoLocations = input()
likeArray = ([0,0,0])

def saveFrames(videos):
    imageArray = np.array(["N","FrameNumber","Height","Width","intensityValue"])
    video = cv2.VideoCapture(videos)
    success, image = video.read()
    count = 1
    while success:
        width, height, channel = image.shape
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        data = asarray(gray)
        #print(data)
        #cv2.imwrite("frame%d.jpg" % count, gray)
        success, image = video.read()
        count += 1
        #imageArray = np.append(data, values="axis")
        imageArray = np.append(imageArray,[1, count, height, width, 1])
    print(np.shape(imageArray))
    np.save(outFile, imageArray)


saveFrames(videoLocations)
