import pyautogui as gui
from time import sleep

sleep(3)
while True:
    try:
        img = gui.locateCenterOnScreen('capturar.png', confidence=0.7)
        gui.mouseDown(img.x, img.y)
        sleep(0.3)
        gui.mouseUp()
    except:
        sleep(0.2)
        print('where is the stone?')
