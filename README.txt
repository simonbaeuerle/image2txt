#### Configure Anaconda environment

Required packages are listed in ./requirements.txt

Create a new anaconda environment from the txt file with:

"conda create -n yourEnvName --file requirements.txt"


#### Install tesseract from https://github.com/UB-Mannheim/tesseract/wiki

#### Update path variables in ./flashCards.py
root = ... -> root folder of this repository

FOlder according to your tesseract installation:
pytesseract.pytesseract.tesseract_cmd = ...
TESSDATA_PREFIX = ...