import pyautogui as gui
from time import sleep

blocks = 0
img = gui.locateCenterOnScreen('capturar.png', confidence=0.8)

sleep(3)
while True:
    if img is not None:
        img = gui.locateCenterOnScreen('capturar.png', confidence=0.8)
        gui.mouseDown(img.x, img.y)
        sleep(1)
        gui.mouseUp()
        print('destroy block')
        blocks += 1
        print(f'destroyed blocks {blocks}')
    else:
        sleep(0.2)
        print('where is the stone?')
   
