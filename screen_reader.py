import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import pyautogui
import cv2
import numpy as np

def read_screen_text():
    screenshot = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    text = pytesseract.image_to_string(image)
    print("🖥️ Screen text captured.")
    return text
