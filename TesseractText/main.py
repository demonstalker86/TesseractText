""" Python-tesseract - это инструмент оптического распознавания символов (OCR) для Python\
То есть он распознает и «прочитает» текст, встроенный в изображения """
import pytesseract
from PIL import Image

img1 = Image.open('foto_text.jpg')
img2 = Image.open('foto_text.png')
pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Users\demonstalker show\AppData\Local\Tesseract-OCR\tesseract.exe'


CUSTOM_CONFIG = r'--psm 6 --oem 3 -l eng+rus'


text1 = pytesseract.image_to_string(img1,  config=CUSTOM_CONFIG)
text2 = pytesseract.image_to_string(img2,  config=CUSTOM_CONFIG)
print(text1, text2)


with open('foto_text1.txt', 'w') as text_file:
    text_file.write(text1)

with open('foto_text2.txt', 'w') as text_file:
    text_file.write(text2)
