from email.mime import image
import cv2
import pytesseract

pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

placa = [
    pytesseract.image_to_string(
    cv2.imread('placa.png', cv2.IMREAD_GRAYSCALE))
]
image = cv2.imread('placa.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Placa', image)
cv2.moveWindow('Placa', 0, 0)
cv2.waitKey(0)
