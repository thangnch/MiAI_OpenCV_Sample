import cv2
import imutils
camera = cv2.VideoCapture('sample.mp4')
current_angle = 0
while (True):
    ret, frame = camera.read()
    if ret:
        if current_angle!=0:
            frame = imutils.rotate(frame,current_angle)
        cv2.imshow("Picture", frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('a'):
        current_angle = 90
    elif key==ord('d'):
        current_angle = -90
    elif key==ord('s'):
        current_angle = 0

camera.release()
cv2.destroyAllWindows()