
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# side note: sword or armor that u enchant doesnt affect the amount of xp given

# to stop the script, hover mouse to top left corner of your screen

import pyautogui as pag
import time
import random

pag.FAILSAFE = True
time.sleep(1.5)

while True:
    pag.write('rpg transmute s')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))