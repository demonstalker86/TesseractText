""" Python-tesseract - это инструмент оптического распознавания символов (OCR) для Python\
То есть он распознает и «прочитает» текст, встроенный в изображения """
import pytesseract
import cv2
import numpy as np

img1 = cv2.imread('foto_text.jpg')
img2 = cv2.imread('foto_text1.jpg')
pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Users\demonstalker show\AppData\Local\Tesseract-OCR\tesseract.exe'

CUSTOM_CONFIG = r'--psm 6 --oem 3 -l eng+rus'

gray_image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
binary_image1 = cv2.threshold(gray_image1 ,130,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
binary_image2 = cv2.threshold(gray_image2 ,130,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
inverted_bin1 = cv2.bitwise_not(binary_image1)
inverted_bin2 = cv2.bitwise_not(binary_image2)
kernel = np.ones((2,2),np.uint8)
processed_img1 = cv2.erode(inverted_bin1, kernel, iterations = 1)
processed_img1 = cv2.dilate(processed_img1, kernel, iterations = 1)
processed_img2 = cv2.erode(inverted_bin2, kernel, iterations = 1)
processed_img2= cv2.dilate(processed_img2, kernel, iterations = 1)

text1 = pytesseract.image_to_string(processed_img1,  config=CUSTOM_CONFIG)
print(text1.strip())
text2 = pytesseract.image_to_string(processed_img2,  config=CUSTOM_CONFIG)
print(text2.strip())


with open('foto_text1.txt', 'w') as text_file:
    text_file.write(text1.strip())

with open('foto_text2.txt', 'w') as text_file:
    text_file.write(text2.strip())
