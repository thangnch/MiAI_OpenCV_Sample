import cv2
import imutils
img = cv2.imread('sample.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thres = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,10)

contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=False)

number = 0
# loop over our contours
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    print(x, y, w, h)
    #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # approximate the contour
    if (85<w<150) and(100<h<150):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        number +=1

print("Number of Contours found = " + str(number))
#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


cv2.imshow('Pix',img)
#cv2.imshow('Thres',thres)
cv2.waitKey()
cv2.destroyAllWindows()