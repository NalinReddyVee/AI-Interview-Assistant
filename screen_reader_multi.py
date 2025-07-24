import mss
import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import Image
from config import TARGET_MONITOR

def capture_screen_text(monitor_number=TARGET_MONITOR):
    with mss.mss() as sct:
        for i, monitor in enumerate(sct.monitors):
            print(f"Monitor {i}: {monitor}")

        monitor = sct.monitors[monitor_number]
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        text = pytesseract.image_to_string(img)
        return text
