import pyautogui as pag
import time
import random

def sell(item,amount):
    pag.write(f'rpg sell {item} {amount}')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))

def craft(item,amount):
    pag.write(f'rpg craft {item} {amount}')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))

def cook(item,amount):
    pag.write(f'rpg cook {item} {amount}')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))

def dismantle(item,amount):
    pag.write(f'rpg dismantle {item} {amount}')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))

def trade(value,amount):
    pag.write(f'rpg trade {value} {amount}')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))
    
def open_lb(lootbox):
    pag.write(f'rpg open {lootbox} all')
    pag.keyDown('enter')
    pag.keyUp('enter')
    time.sleep(random.randint(1,2))