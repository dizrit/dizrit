import pyautogui
import os, sys, time
import random
pyautogui.FAILSAFE= False

def pushNumber():
    randNumber = random.randint(1, 30)
    for pushNumber in range(randNumber):
        pyautogui.press("pageup")
        time.sleep(1)
        pyautogui.press("pageup")
        pyautogui.scroll(-10)
        def randPush():
            randPushN = random.randint(1, 10)
            for randPush in range(randPushN):
                randMouse = random.randint(5, 1500)
                pyautogui.moveTo(randMouse, 1, duration =1)
                pyautogui.click()
                pyautogui.click()
                rand1time = random.uniform(0.5, 1.5)
                time.sleep(rand1time)
                randMouse2 = random.randint(170, 910)
                pyautogui.moveTo(1915, randMouse2, duration =1)
                pyautogui.click()
                pyautogui.click()
                rand2time = random.uniform(0.5, 1.5)
                time.sleep(rand2time)
        randPush()
        pyautogui.press("pagedown")
        time.sleep(1)
        pyautogui.press("pagedown")
        pyautogui.scroll(10) 

def pause():
    randPause3 = random.randint(1, 275)
    time.sleep(randPause3)
    if randPause3 <= 30:
        pause()

try:
    while True:
        pushNumber()
        pause()

except KeyboardInterrput:
    print('\n')
