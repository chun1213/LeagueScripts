
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import keyboard
import mss
import numpy
import pytesseract
from PIL import Image
import cv2
import datetime
import numpy as np
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

toggle=0;
level=0;
prev_valid=0;
monitor = {'top': 39, 'left': 210, 'width': 48, 'height': 16}
monitor2 = {'top': 990, 'left': 588, 'width': 18, 'height': 18}
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "D:\Program Files (x86)\Tesseract-OCR\tessdata" --psm 8 --oem 4 -c tessedit_char_whitelist=0123456789'
damage=0
while True:
    if keyboard.is_pressed('o'):  # if key 'q' is pressed
        toggle=0
    elif keyboard.is_pressed('i'):
        toggle=1
    if toggle==1:
        text = 0;
        start = datetime.datetime.now()
        with mss.mss() as sct:
            img = sct.grab(monitor)
            img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            img = img.resize((200, 200));
            img.save('test.png', dpi=(300.0, 300.0))
            image = cv2.imread('test.png')
            gray = get_grayscale(image)
            try:
                text = int(pytesseract.image_to_string(gray, lang='eng', config=tessdata_dir_config))
                print(text)
            except:
                print("none")
        if level==1:
            damage = 390
        elif level==2:
            damage = 410
        elif level==3:
            damage = 430
        elif level==4:
            damage = 450
        elif level==5:
            damage = 480
        elif level==6:
            damage = 510
        elif level==7:
            damage = 540
        elif level==8:
            damage = 570
        elif level==9:
            damage = 600
        elif level==10:
            damage = 640
        elif level==11:
            damage = 680
        elif level==12:
            damage = 720
        elif level==13:
            damage = 760
        elif level==14:
            damage = 800
        elif level==15:
            damage = 850
        elif level==16:
            damage = 900
        elif level==17:
            damage = 950
        elif level==18:
            damage = 1000
        if text!=0 and text>400:
            prev_valid=text
        if damage>int(text) and text!=0 and text>prev_valid-800:
            keyboard.send('a')
            toggle=0
        finish = datetime.datetime.now()
        print (finish - start)
    if keyboard.is_pressed('p'):
        with mss.mss() as sct:
            img2 = sct.grab(monitor2)
            img2 = Image.frombytes("RGB", img2.size, img2.bgra, "raw", "BGRX")
            img2= img2.resize((200,200));
            img2.save('test2.png', dpi=(300.0, 300.0))
            image = cv2.imread('test2.png')
            gray = get_grayscale(image)
            try:
                level = int(pytesseract.image_to_string(gray, lang='eng', config=tessdata_dir_config))
                print(level)
            except:
                print("none")
