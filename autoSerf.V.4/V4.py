import pyautogui
import os, sys, time
import random
pyautogui.FAILSAFE= False

timeLst = [7, 52, 86, 121, 177, 269]

def pushNumber():
    randNumber = random.randint(1, 20)
    for pushNumber in range(randNumber):
        def randPush():
            randPushN = random.randint(1, 30)
            for randPush in range(randPushN):
                randMouse = random.randint(5, 1500)
                pyautogui.moveTo(randMouse, 1, duration =1)
                pyautogui.click()
                rand1time = random.uniform(0.5, 1.5)
                time.sleep(rand1time)
                randMouse2 = random.randint(170, 910)
                pyautogui.moveTo(1915, randMouse2, duration =1)
                pyautogui.click()
                rand2time = random.uniform(0.5, 1.5)
                time.sleep(rand2time)
        randPush()

def keys():
    numberKeys = random.randint(1, 20)
    for keys in range(numberKeys):
        def keyU():
            randUp = random.randint(1, 5)
            for keyU in range(randUp):
                pyautogui.press("pageup")
                pyautogui.scroll(-10)
                randPause1 = random.uniform(1, 2)
                time.sleep(randPause1)
        def keyD():
            randDown = random.randint(1, 6)
            for keyD in range(randDown):
                pyautogui.press("pagedown")
                pyautogui.scroll(10) 
                randPause2 = random.uniform(1, 2)
                time.sleep(randPause2)
            if randDown >= 5:
                pyautogui.press("home")
        keyU()
        keyD()

def pause():
    randPause3 = random.choice(timeLst)
    time.sleep(randPause3)

try:
    while True:
        pushNumber()
        keys()
        pause()

except KeyboardInterrput:
    print('\n')
