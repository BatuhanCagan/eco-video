import os
import numpy as np
import cv2
import pandas as pd


def saveFrames():
    csvList = pd.read_csv('recordset.csv')
    funcVids = list(i for i in csvList.iloc[:,1])
    outFile = "frames.npy"
    videoList = []
    for videos in funcVids:
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