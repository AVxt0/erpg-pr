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
        print('Only accepts area that are major trade points\n')
        area = int(input('Area:  '))
        if area == 3:
            fish = int(input('Fish:  '))
            a5apple = fish/2
            print(f'A5 apple: {a5apple}')
            a10wood = fish * 17.08
            print(f'A10 wood: {a10wood}')
        elif area == 5:
            apple = int(input('Apples:  '))
            a10wood = apple * 33.75
            print(f'A10 wood: {a10wood}')
        elif area == 8:
            apple = int(input('Apples:  '))
            a10wood = apple * 2.25
            print(f'A10 wood: {a10wood}')
        elif area == 9:
            fish = int(input('Fish:  '))
            a10wood = fish * 1.5
            print(f'A10 wood: {a10wood}')
        else: 
            print('Invalid Input')
            print('Exiting Program')
            time.sleep(1)
            break
    elif calc_type == '2':
        
    else:
        print('Invalid Input')
        print('Exiting Program')
        time.sleep(1)
        break

    print('')
    restart = input('Continue? (y/n):  ')
    if restart.lower() == 'n' or 'no':
        break
    elif restart.lower() == 'y' or 'yes':
        continue
    else:
        print('Invalid Input')
        print('Exiting Program')
        time.sleep(1)
        break