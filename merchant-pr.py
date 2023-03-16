
# Be sure to keep an eye on ur discord every now and then
# just try to not get into jail xdd

# side note: dismantles everything in your inventory
# sells mob drops too
# wooden logs are sold in batches of 50k because more money lol
# if you want to do it all at once, just stop the script once it finishes
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

# opens lootboxes

pag.write('rpg open g all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg open o all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2)) 
pag.write('rpg open ed all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg open ep all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg open r all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg open u all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg open c all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))

# mats

pag.write('rpg dismantle epic fish all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle golden fish all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle trade a all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle banana all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle trade c all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle trade e all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle ultra log all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle hyper log all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle mega log all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle super log all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg dismantle epic log all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))

# end game items

pag.write('rpg sell ultimate log all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell super fish all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell watermelon all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))

# mob drops

pag.write('rpg sell wolf skin all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell zombie eye all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell unicorn horn all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell mermaid hair all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell chip all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell dragon scale all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))

# farm items

pag.write('rpg sell bread all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell carrot all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sellpotato all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell seed all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell bread seed all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell carrot seed all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell potato seed all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))

# misc items

pag.write('rpg sell life potion all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell flasks all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))
pag.write('rpg sell lottery ticket all')
pag.keyDown('enter')
pag.keyUp('enter')
time.sleep(random.randint(1,2))

while True:
    pag.write('rpg sell wooden log 50k')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))