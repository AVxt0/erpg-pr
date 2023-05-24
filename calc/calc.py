import pyautogui as pag
import time
import random
import erpg

pag.FAILSAFE = True

print('----- EPIC RPG Related Calculator -----\n')
print('1. A10 Mats Calculator')
print('2. Crafting calculator\n')

while True:
    calc_type = input('Enter your choice (1/2):  ')
    print('')

    if calc_type == '1':
        area = input('Area:  ')
        if area == '3':
            