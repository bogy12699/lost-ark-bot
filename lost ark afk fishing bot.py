import pyautogui as pg
import keyboard
import time
import random
import timeout_decorator


while True:

    #PESCUIESTE CATEA

    for i in range(15):
        time.sleep(random.randint(6,8))
        pg.moveTo(945, 814, 1)
        pg.hotkey('e')
        start = time.time()
        while True:
            
            if pg.pixel(961, 475) [0] == 220:
                time.sleep(0.3)
                pg.hotkey('e')
                break
            elif time.time() - start > 27:
                break
        

    #REPARA CATEA

    time.sleep(2)
    pg.hotkey('alt','p')
    pg.leftClick(1201, 705, 1, 1)
    pg.leftClick(1239, 982, 1, 1)
    pg.leftClick(735, 808, 1, 1)
    pg.leftClick(894, 631, 1, 1)
    time.sleep(1)
    pg.press("esc")
    time.sleep(1)
    pg.press("esc")
    







