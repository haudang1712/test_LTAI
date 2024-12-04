# -*- coding: utf-8 -*-
"""test_LTAI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aztGxs83Ckupn4w7ADVR1r3Oh70keeG9
"""

!pip install pytesseract

!sudo apt install tesseract-ocr

try:
 from PIL import Image
except ImportError:
 import Image
import cv2
import pytesseract

img = cv2.imread('test.jpg')

lang = 'vie'
config = r'--oem 3 --psm 6'
extractedInformation = pytesseract.image_to_string(img)
print(extractedInformation)

