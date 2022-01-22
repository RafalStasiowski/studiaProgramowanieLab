import time
import cv2 as cv

net = cv.dnn_DetectionModel('frozen_inference_graph.pb', 'graph.pbtxt')
net.setInputSize(320, 320)
net.setInputScale(1.05 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)
cap = cv.VideoCapture(0)

while True:

    r, img = cap.read()
    counter = 0
    start_time = time.time()
    classes, confidences, boxes = net.detect(img, confThreshold=0.6)
    end_time = time.time()
    try:
        for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
            if classId == 1:
                counter += 1
                cv.rectangle(img, box, color=(0, 255, 0), thickness=3)
    except:
        pass

    print("Czas: " + (end_time - start_time).__str__())

    img = cv.putText(img, "Ile ludzi: " + counter.__str__(), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                     cv.LINE_AA)

    img = cv.putText(img, "FPS: " + int(round(((1.0) / (end_time - start_time)))).__str__(), (50, 100),
                     cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
    cv.imshow('Rezultat', img)

    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break

