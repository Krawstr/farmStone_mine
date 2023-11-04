import pyautogui as gui
from time import sleep

procurar = 'sim'
sleep(3)
while procurar == 'sim':
    try:
        img = gui.locateCenterOnScreen('capturar.png', confidence=0.7)
        gui.mouseDown(img.x, img.y)
        sleep(0.3)
        gui.mouseUp()
    except:
        sleep(0.2)
        print('cade pedra?')
