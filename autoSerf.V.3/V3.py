import pyautogui
import os, sys, time
import random
pyautogui.FAILSAFE= False

def pushNumber():
    randNumber = random.randint(1, 10)
    for pushNumber in range(randNumber):
        def randPush():
            randPushN = random.randint(37, 64)
            for randPush in range(randPushN):
                randMouse = random.randint(1, 11)
                if randMouse == 1:
                    pyautogui.moveTo(150, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 2:
                    pyautogui.moveTo(250, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 3:
                    pyautogui.moveTo(400, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 4:
                    pyautogui.moveTo(500, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 5:
                    pyautogui.moveTo(650, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 6:
                    pyautogui.moveTo(750, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 7:
                    pyautogui.moveTo(900, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 8:
                    pyautogui.moveTo(1000, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 9:
                    pyautogui.moveTo(1150, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 10:
                    pyautogui.moveTo(1300, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
                if randMouse == 11:
                    pyautogui.moveTo(1400, 1, duration=1)
                    pyautogui.click()
                    randPause = random.uniform(0.5, 1.5)
                    time.sleep(randPause)
        randPush()

def keys():
    numberKeys = random.randint(1, 10)
    for keys in range(numberKeys):
        def keyU():
            randUp = random.randint(1, 5)
            for keyU in range(randUp):
                pyautogui.press("pageup")
                randPause1 = random.uniform(1, 3)
                time.sleep(randPause1)
        def keyD():
            randDown = random.randint(1, 6)
            for keyD in range(randDown):
                pyautogui.press("pagedown")
                randPause2 = random.uniform(1, 3)
                time.sleep(randPause2)
            if randDown >= 5:
                pyautogui.press("home")
        keyU()
        keyD()

def pause():
    randPause3 = random.randint(10, 191)
    time.sleep(randPause3)
    if randPause3 <= 30:
        pause()

try:
    while True:
        pushNumber()
        keys()
        pause()

except KeyboardInterrput:
    print('\n')
