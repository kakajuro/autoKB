import keyboard as kb
from split import split
from pynput.keyboard import Key, Controller
import pyautogui
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

keyboard = Controller()

print("Initiating...")
time.sleep(5)

# 1003 656

if pyautogui.pixel(999, 661)[1] == 208: 
    while kb.is_pressed('esc') == False:
        img = pyautogui.screenshot(region=(952, 706, 500, 500))
        #img.save(r"currentLetter.png")

        letters = pytesseract.image_to_string(img, config='tessedit_char_whitelist=0123456789')
        #print(letters)
        lettersArray = split(letters)
        #print(lettersArray)
        key = lettersArray[0].lower()
        isSpace = letters[1]
        print(key, isSpace)

        if lettersArray[0] == '\x0c':
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(0.2)
        elif lettersArray[1] == ' ':
            keyboard.press(key)
            keyboard.release(key)
            time.sleep(0.2)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(0.2)
        else:
            keyboard.press(key)
            keyboard.release(key)
            time.sleep(0.2)







