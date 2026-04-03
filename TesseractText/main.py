""" Python-tesseract - это инструмент оптического распознавания символов (OCR) для Python\
То есть он распознает и «прочитает» текст, встроенный в изображения """
import pytesseract
import cv2
import numpy as np
import os

print("Текущая рабочая папка:", os.getcwd() + "\n\n")

img1 = cv2.imread('foto_text.jpg')
if img1 is None:
    print('Файл foto_text.jpg не найден!')
    exit(1)

img2 = cv2.imread('foto_text1.jpg')
if img2 is None:
    print('Файл foto_text1.jpg не найден!')
    exit(1)

try:
    from local_config import TESSERACT_PATH
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
except ImportError:
    # Если файла нет, можно либо выдать ошибку, либо использовать путь по умолчанию
    print("Предупреждение: local_config.py не найден. Tesseract может не работать.")

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

text1 = pytesseract.image_to_string(processed_img1, config=CUSTOM_CONFIG).strip()
text2 = pytesseract.image_to_string(processed_img2, config=CUSTOM_CONFIG).strip()

print(text1 + "\n\n" + text2)


with open('foto_text1.txt', 'w') as text_file:
    text_file.write(text1.strip())

with open('foto_text2.txt', 'w') as text_file:
    text_file.write(text2.strip())