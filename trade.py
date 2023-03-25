
# side note: only the major trades

import pyautogui as pag
import time
import random
import erpg

pag.FAILSAFE = True
area = pag.prompt('What area are you in?')
time.sleep(0.5)
pag.confirm('Starting in 1 second')
time.sleep(1)


def area_3():
    erpg.dismantle('epic fish')
    erpg.dismantle('golden fish')

    erpg.dismantle('banana')
    erpg.trade('c')

    erpg.dismantle('ultra log')
    erpg.dismantle ('hyper log')
    erpg.dismantle('mega log')
    erpg.dismantle('super log')
    erpg.dismantle('epic log')
    erpg.trade('b')

def area_5():
    erpg.dismantle('epic fish')
    erpg.dismantle('golden fish')
    erpg.trade('a')

    erpg.dismantle('banana')

    erpg.trade('e')

    erpg.dismantle('ultra log')
    erpg.dismantle ('hyper log')
    erpg.dismantle('mega log')
    erpg.dismantle('super log')
    erpg.dismantle('epic log')
    erpg.trade('d')

def area_7():
    erpg.dismantle('epic fish')
    erpg.dismantle('golden fish')
    erpg.trade('a')

    erpg.dismantle('banana')
    erpg.trade('c')

    erpg.trade('e')

    erpg.dismantle('ultra log')
    erpg.dismantle ('hyper log')
    erpg.dismantle('mega log')
    erpg.dismantle('super log')
    erpg.dismantle('epic log')

def area_9():
    erpg.dismantle('epic fish')
    erpg.dismantle('golden fish')

    erpg.dismantle('banana')
    erpg.trade('c')

    erpg.trade('e')

    erpg.dismantle('ultra log')
    erpg.dismantle ('hyper log')
    erpg.dismantle('mega log')
    erpg.dismantle('super log')
    erpg.dismantle('epic log')
    erpg.trade('b')

def area_10():
    erpg.dismantle('epic fish')
    erpg.dismantle('golden fish')
    erpg.trade('a')

erpg.open_lb('g')
erpg.open_lb('o')
erpg.open_lb('ed')
erpg.open_lb('ep')
erpg.open_lb('r')
erpg.open_lb('u')
erpg.open_lb('c')

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