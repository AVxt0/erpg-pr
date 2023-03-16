
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# side note: dismantles everything in your inventory
# sells all mod drops
# read this before !!!!!!!!!

# to stop the script, hover mouse to top left corner of your screen

import pyautogui as pag
import time
import random

pag.FAILSAFE = True
time.sleep(0.5)
print('starting in 1 second')
time.sleep(1)

def sell(item):
    pag.write(f'rpg sell {item} all')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))

def dismantle(item):
    pag.write(f'rpg dismantle {item} all')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))

def trade(value):
    pag.write(f'rpg trade {value} all')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    
def open_lb(lootbox):
    pag.write(f'rpg open {lootbox} all')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))

# opens lootboxes

open_lb('g')
open_lb('o')
open_lb('ed')
open_lb('ep')
open_lb('r')
open_lb('u')
open_lb('c')

# mats

dismantle('epic fish')
dismantle('golden fish')
trade('a')

dismantle('banana')
trade('c')

trade('e')

dismantle('ultra log')
dismantle ('hyper log')
dismantle('mega log')
dismantle('super log')
dismantle('epic log')
sell('wooden log')

# end game items

sell('ultimate log')
sell('super fish')
sell('watermelon')

# mob drops

sell('wolf skin')
sell('zombie eye')
sell('unicorn horn')
sell('mermaid hair')
sell('chip')
sell('dragon scale')

# farm items

sell('bread')
sell('carrot')
sell('potato')
sell('seed')
sell('bread seed')
sell('carrot seed')
sell('potato seed')

# misc items

sell('life potion')
sell('flasks')
sell('lottery ticket')