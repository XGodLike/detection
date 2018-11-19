#coding : utf-8
import cv2
import os
import time
import numpy as np
from time import sleep


count = 1
path = 'F:\\Python\\face_detector\\img'


def checkPath(path):
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == "__main__":

    label=np.empty(400)
    for i in range(400):
        label[i*10:i*10+10] = i
    label=label.astype(np.int)
    checkPath(path)

    # img = cv2.imread("1.jpg")
    #
    # cv2.namedWindow("Image")
    # cv2.imshow("Image",img)
    # cv2.waitKey(0)
    #
    # cv2.destroyAllWindows()
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture()
    #RetValue = video_capture.open("F:\\Python\\face_detector\\test_data\\1.avi")
    RetValue = video_capture.open(0)



    count = 0
    while True:
        if not RetValue:
            print('Unable to load camera.')
            sleep(5)
            pass


        ret, frame = video_capture.read()
        cv2.imshow('frame', frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            break
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=5,
            minSize=(5, 5),
            # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow('Video', frame)
                #########
                img_rsize = cv2.resize(gray[y: (y + h),x:(x+ w)],(64,64))
                name = str(int(time.time())) + str(count) + '.jpg'
                cv2.imwrite(path + os.sep + name,img_rsize)
                print r"get %d img" % count
                count += 1

                #cv2.imshow('Video', img_rsize)

        time.sleep(0.5)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video_capture.release()


    cv2.destroyAllWindows()