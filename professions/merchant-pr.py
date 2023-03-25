
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# side note: erpg.dismantles everything in your inventory
# sells all mod drops
# read this before !!!!!!!!!

# to stop the script, hover mouse to top left corner of your screen

import pyautogui as pag
import time
import random
import erpg

pag.FAILSAFE = True
time.sleep(0.5)
pag.confirm('starting in 1 second','merchant-pr.py')
time.sleep(1)

# opens lootboxes

erpg.open_lb('g')
erpg.open_lb('o')
erpg.open_lb('ed')
erpg.open_lb('ep')
erpg.open_lb('r')
erpg.open_lb('u')
erpg.open_lb('c')

# mats

erpg.dismantle('epic fish','all')
erpg.dismantle('golden fish','all')
erpg.trade('a','all')

erpg.dismantle('banana','all')
erpg.trade('c','all')

erpg.trade('e','all')

erpg.dismantle('ultra log','all')
erpg.dismantle ('hyper log','all')
erpg.dismantle('mega log','all')
erpg.dismantle('super log','all')
erpg.dismantle('epic log','all')
erpg.sell('wooden log','all')

# end game items

erpg.sell('ultimate log','all')
erpg.sell('super fish','all')
erpg.sell('watermelon','all')

# mob drops

erpg.sell('wolf skin','all')
erpg.sell('zombie eye','all')
erpg.sell('unicorn horn','all')
erpg.sell('mermaid hair','all')
erpg.sell('chip','all')
erpg.sell('dragon scale','all')

# farm items

erpg.sell('bread','all')
erpg.sell('carrot','all')
erpg.sell('potato','all')
erpg.sell('seed','all')
erpg.sell('bread seed','all')
erpg.sell('carrot seed','all')
erpg.sell('potato seed','all')

# misc items

erpg.sell('life potion','all')
erpg.sell('flask','all')
erpg.sell('lottery ticket','all')