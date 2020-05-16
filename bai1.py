import cv2

camera = cv2.VideoCapture(0)

while (True):
    ret, frame = camera.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Picture", gray)
    if cv2.waitKey(1)==ord('q'):
        break

camera.close()
cv2.destroyAllWindows()