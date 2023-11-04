import pyautogui as gui
from time import sleep

search = 'sim'
sleep(3)
while search == 'sim':
    try:
        img = gui.locateCenterOnScreen('capturar.png', confidence=0.7)
        gui.mouseDown(img.x, img.y)
        sleep(0.3)
        gui.mouseUp()
    except:
        sleep(0.2)
        print('cade pedra?')
