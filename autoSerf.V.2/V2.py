import pyautogui
import os, sys, time
import random
pyautogui.FAILSAFE= False

lstPause = [9, 12, 35, 67, 94, 128]

def randPush():
    randPushN = random.randint(1, 20)
    for randPush in range(randPushN):
        randMouse = random.randint(1, 6)
        if randMouse == 1:
            pyautogui.moveTo(150, 1, duration=1)
            pyautogui.click()
            randPause = random.uniform(0.5, 2)
            time.sleep(randPause)
        if randMouse == 2:
            pyautogui.moveTo(400, 1, duration=1)
            pyautogui.click()
            randPause = random.uniform(0.5, 2)
            time.sleep(randPause)
        if randMouse == 3:
            pyautogui.moveTo(650, 1, duration=1)
            pyautogui.click()
            randPause = random.uniform(0.5, 2)
            time.sleep(randPause)
        if randMouse == 4:
            pyautogui.moveTo(900, 1, duration=1)
            pyautogui.click()
            randPause = random.uniform(0.5, 2)
            time.sleep(randPause)
        if randMouse == 5:
            pyautogui.moveTo(1150, 1, duration=1)
            pyautogui.click()
            randPause = random.uniform(0.5, 2)
            time.sleep(randPause)
        if randMouse == 6:
            pyautogui.moveTo(1400, 1, duration=1)
            pyautogui.click()
            randPause = random.uniform(0.5, 2)
            time.sleep(randPause)

def keyu():
    randUp = random.randint(1, 15)
    for keyu in range(randUp):
        pyautogui.press("pageup")
        randPause1 = random.uniform(1, 3)
        time.sleep(randPause1)

def keyd():
    randDown = random.randint(1, 15)
    for keyu in range(randDown):
        pyautogui.press("pagedown")
        randPause2 = random.uniform(1, 3)
        time.sleep(randPause2)
    if randDown >= 6:
        pyautogui.press("home")

def pause():
    randPause3 = random.choice(lstPause)
    time.sleep(randPause3)

try:
    while True:
        randPush()
        keyu()
        keyd()
        randPush()
        randPush()
        randPush()
        randPush()
        randPush()
        randPush()
        randPush()
        randPush()
        randPush()
        keyu()
        keyd()
        randPush()
        randPush()
        randPush()
        randPush()
        randPush() 
        randPush()
        randPush()
        randPush()
        randPush()
        randPush()
        pause()

except KeyboardInterrput:
    print('\n')
