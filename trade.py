
# side note: only the major trades

import pyautogui as pag
import time
import random

pag.FAILSAFE = True
area = pag.prompt('What area are you in?')
time.sleep(0.5)
pag.confirm('Starting in 1 second')
time.sleep(1)

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

def area_3():
    dismantle('epic fish')
    dismantle('golden fish')

    dismantle('banana')
    trade('c')

    dismantle('ultra log')
    dismantle ('hyper log')
    dismantle('mega log')
    dismantle('super log')
    dismantle('epic log')
    trade('b')

def area_5():
    dismantle('epic fish')
    dismantle('golden fish')
    trade('a')

    dismantle('banana')

    trade('e')

    dismantle('ultra log')
    dismantle ('hyper log')
    dismantle('mega log')
    dismantle('super log')
    dismantle('epic log')
    trade('d')

def area_7():
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

def area_9():
    dismantle('epic fish')
    dismantle('golden fish')

    dismantle('banana')
    trade('c')

    trade('e')

    dismantle('ultra log')
    dismantle ('hyper log')
    dismantle('mega log')
    dismantle('super log')
    dismantle('epic log')
    trade('b')

def area_10():
    dismantle('epic fish')
    dismantle('golden fish')
    trade('a')

open_lb('g')
open_lb('o')
open_lb('ed')
open_lb('ep')
open_lb('r')
open_lb('u')
open_lb('c')

if area == 3:
    area_3()
elif area == 5 or area == 8:
    area_5()
elif area == 7:
    area_7()
elif area == 9:
    area_9()
elif area == 10:
    area_10()
else:
    print('invalid input')
    print('exiting script')
    time.sleep(2)
    exit