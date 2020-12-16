import keyboard as kb
from split import split
from pynput.keyboard import Key, Controller
from dotenv import load_dotenv
import os
import pyautogui
import time
import random
import pytesseract
load_dotenv()

path=os.getenv('PATH_LINK')

pytesseract.pytesseract.tesseract_cmd = path

keyboard = Controller()
mouse = Controller()

print("Initiating...")
canStart = False
time.sleep(2)

def pressKey(keyToPress):
    keyboard.press(keyToPress)
    keyboard.release(keyToPress)
    sleepTime = random.uniform(0.01, 0.2)
    time.sleep(sleepTime)
    
def ifSame(listOfStrings):
    result = False
    if len(listOfStrings) > 0 :
        result = all(elem == listOfStrings[0] for elem in listOfStrings)
        
    if result :
        return True
    else:        
        return False
    
start = pyautogui.locateCenterOnScreen('./imgs/retry.png')
pyautogui.moveTo(start)
pyautogui.click(pyautogui.position())
time.sleep(0.2)

#693, 450

timer = pyautogui.screenshot(region=(688, 450, 80, 65))
timer.save(r"thing.png")
timerTime = pytesseract.image_to_string(timer, config='tessedit_char_whitelist=0123456789')
timerTimeArray = split(timerTime)
print(timerTimeArray)

if timerTimeArray[0] == "6" and timerTimeArray[1] == "0":
    canStart = True
else:
    canStart = False

if canStart: 
    isEnough = False
    lastKey = ["wrhj80h8v", "ksodfjpsdofs", "jr09hf340uithg"]
    
    while kb.is_pressed('esc') == False:
        #Check the try again pixel
        time.sleep(0.2)
        img = pyautogui.screenshot(region=(952, 706, 500, 500))
        #img.save(r"currentLetter.png")
        print(lastKey)
        areTheSame = ifSame(lastKey)
        
        if areTheSame == True:
            pressKey(letters[-1])

        letters = pytesseract.image_to_string(img, config='tessedit_char_whitelist=0123456789')
        print(letters)
        lettersArray = split(letters)
        #print(lettersArray)
        key = lettersArray[0].lower()
        isSpace = letters[1]
        #print(key, isSpace)

        if lettersArray[0] == '\x0c':
            pressKey(Key.space)
        elif lettersArray[1] == ' ':
            if len(lastKey) > 3:
                check = ifSame(lastKey)
                if check:
                    print("y")
                else:
                    print("n")
                    lastKey.insert(0, key)
                    pressKey(key)
                    pressKey(Key.space)
                    del lastKey[-1:]
            else:
                lastKey.insert(0, key)
                pressKey(key)
                pressKey(Key.space)
                del lastKey[-1:]
        else:
            if len(lastKey) > 3:
                del lastKey[-1:]
                check = ifSame(lastKey)
                if check:
                    print("y")
                else:
                    print("n")
                    lastKey.insert(0, key)
                    pressKey(key)
                    del lastKey[-1:]
            else:
                lastKey.insert(0, key)
                pressKey(key)
                del lastKey[-1:]