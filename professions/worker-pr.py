
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# makes 100 banana pickaxe in batches

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
    erpg.trade('d','150')
    erpg.craft('banana','100')
    erpg.craft('epic log','60000')
    erpg.craft('super log','6000')
    erpg.craft('mega log','600')
    erpg.cook('banana pickaxe','100')