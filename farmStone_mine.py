import pyautogui as gui
from time import sleep

blocks = 0

sleep(3)
while True:
    try:
        img = gui.locateCenterOnScreen('capturar.png', confidence=0.8)
        gui.mouseDown(img.x, img.y)
        sleep(1)
        gui.mouseUp()
        print('destry block')
        blocks += 1
        print(f'destroyed blocks {blocks}')
    except:
        sleep(0.2)
        print('where is the stone?')
   
