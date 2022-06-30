import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

placa = []

image = cv2.imread('placa1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (3,3))
canny = cv2.Canny(gray, 150, 200)
canny = cv2.dilate(canny, None, iterations=1)
cnts,_ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(image, cnts, -1, (0, 255,0),2)

for c in cnts:
    area = cv2.contourArea(c)

    if area > 15000:
        print('area =', area)
        cv2.drawContours(image, [c], 0, (0, 255,0),2)


cv2.imshow('Image', image)
cv2.imshow('Canny', canny)

cv2.moveWindow('Image', 45, 10)
cv2.waitKey(0)