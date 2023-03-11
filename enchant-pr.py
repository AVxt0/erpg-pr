
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# to stop the script, hover mouse to top left corner of your screen

import pyautogui as pag
import time
import random

pag.FAILSAFE = True

while True:
    pag.write('rpg transmute s')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))