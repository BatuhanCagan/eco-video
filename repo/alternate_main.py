import os
import numpy as np
import cv2
import pandas as pd


def saveFrames():
    csvList = []
    vids = os.listdir()
    get = 'csv'
    funcVid = list(filter(lambda a: any([1 if get in a else 0 for get in get.split(' ')]), vids))
    for f in funcVid:
        fil = pd.read_csv(f)
        for i in range(len(fil)):
            csvList.append(fil.loc[i, "PublicLink"])
    outFile = "frames.npy"
    videoList = []
    for videos in csvList:
        video = cv2.VideoCapture(videos)
        while True:
            success, image = video.read()
            if not success:
                break
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            videoList.append(gray)
    videoList = np.array(videoList).reshape(-1, gray.shape[0], gray.shape[1], 1)
    print(videoList.shape)
    np.save(outFile, videoList)

saveFrames()