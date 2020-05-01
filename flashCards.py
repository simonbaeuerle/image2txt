"""
Read image files from ./imgs_flashCards
Perform OCR scan on images
Save text to txt file

Created 01.05.2020 by Simon Bäuerle
"""

import pytesseract
from PIL import Image 
import os

# Repository root directory
root = "C:\\Users\\Simon\\Git\\image2txt\\"

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
TESSDATA_PREFIX = "C:\\Program Files\\Tesseract-OCR"


# Set working directory to repository root directory
os.chdir(root)

# Path to folder with images to be scanned
path = os.path.join(root, "imgs_flashCards\\")

# Loop over images
result = ""
for i in range(1,5):
    # Image name template
    imgfile = str(i) + ".jpeg"
    
    # Append images to result string
    result += "\n \n ---------------------------------------------------- \n \n"
    result += pytesseract.image_to_string(Image.open(os.path.join(path, imgfile)))

# Output scanned text to txt file
txtFile = open("Output.txt", "w")
txtFile.write(result)
txtFile.close()