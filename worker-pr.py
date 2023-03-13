
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# makes 100 banana pickaxe in batches

# to stop the script, hover mouse to top left corner of your screen

import pyautogui as pag
import time
import random

pag.FAILSAFE = True
time.sleep(1.5)

while True:
    pag.write('rpg trade d 150')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    pag.write('rpg craft banana 100')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    pag.write('rpg craft epic log 60000')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    pag.write('rpg craft super log 6000')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    pag.write('rpg craft mega log 600')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    pag.write('rpg cook banana pickaxe 100')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))