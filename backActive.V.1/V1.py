import pyautogui
import os, sys, time
import random
pyautogui.FAILSAFE= False

lstGlobalP = [11, 12, 13, 21, 32, 51]

def push():
    randKey = random.randint(8, 16)
    for push in range (randKey):
        pyautogui.press("numlock")

        randPause = random.uniform(0.5, 3)
        time.sleep(randPause)

def pauseG():
    globalPause = random.choice(lstGlobalP)
    time.sleep(globalPause)

try:
    while True:

       push()
       pauseG()

except KeyboardInterrput:
    print('\n')