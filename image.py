import time
from os import listdir
from os.path import isfile, join

import cv2 as cv

net = cv.dnn_DetectionModel('frozen_inference_graph.pb', 'graph.pbtxt')
net.setInputSize(320, 320)
net.setInputScale(1.00 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


files = [f for f in listdir("./images/") if isfile(join("./images", f))]
index = 0
flag = True

while True:

    counter = 0

    if flag:
        img = cv.imread("images/" + files[index])
        height, width, channels = img.shape
        start_time = time.time()
        classes, confidences, boxes = net.detect(img, confThreshold=0.52, nmsThreshold=0.4)
        end_time = time.time()

        print("Czas: " + (end_time - start_time).__str__())
        flag = False
        try:
            for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
                if classId == 1:
                    counter += 1
                    cv.rectangle(img, box,
                                 color=(0, 255, 0),
                                 thickness=2)
        except:
            pass
        img = cv.resize(img, (1280, 720))
        img = cv.putText(img, "Ile ludzi: " + counter.__str__(), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                         cv.LINE_AA)
        img = cv.putText(img, "Czas: " + (end_time - start_time).__str__(), (50, 100),
                         cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow('Rezultat', img)

    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        exit()

    if key & 0xFF == ord('n'):
        if (index - 1) < 0:
            index = len(files) - 1
        else:
            index -= 1
        flag = True

    if key & 0xFF == ord('m'):
        index += 1
        index %= len(files)
        flag = True
