
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# crafts in batches of 1000 epic logs

# to stop the script, hover mouse to top left corner of your screen

import pyautogui as pag
import time
import random
import erpg

pag.FAILSAFE = True
time.sleep(0.5)
pag.confirm('starting in 1 second')
time.sleep(1)

while True:
    erpg.craft('epic log','1000')
    erpg.dismantle('epic log','all')