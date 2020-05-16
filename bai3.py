import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

def save_face(frame, faces):
    i=0
    for (x, y, w, h) in faces:
        i+=1
        crop = frame[y:y+h,x:x+w]
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.imwrite("file{}.png".format(i),crop)
    return


camera = cv.VideoCapture(0)

while (True):
    ret, img = camera.read()
    if ret:


        # Chuyen gray
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 10,minSize=(100,100))

        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            qroi_color = img[y:y + h, x:x + w]

        cv.imshow("Picture", img)

    key = cv.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('s'):
        save_face(img, faces)

camera.release()
cv.destroyAllWindows()

