import time
import pyautogui
from tqdm import tqdm
#time.sleep(3)
print(pyautogui.position())
#pyautogui.scroll(200)
for i in range(139):
    print(i)
    total_iteracoes = int(7)
    progresso = tqdm(total=total_iteracoes, desc='Progresso')
    time.sleep(2)
    pyautogui.click(x=1744, y=442) #LAPIS
    progresso.update(1)
    time.sleep(2)
    #pyautogui.click(x=986, y=541) #TEXTO
    #pyautogui.hotkey("shift", "home")
    # pyautogui.moveTo(645, 545)
    # pyautogui.mouseDown()
    # time.sleep(1)
    # pyautogui.moveTo(830, 545)
    # pyautogui.mouseUp()
    # time.sleep(1)
    # pyautogui.hotkey("ctrl", "v")
    # progresso.update(1)
    # time.sleep(1)
    # time.sleep(1)
    pyautogui.click(x=1465, y=627) #ASP
    progresso.update(1)
    time.sleep(1)
    pyautogui.press("up")
    progresso.update(1)
    time.sleep(1)
    pyautogui.press("enter")
    progresso.update(1)
    time.sleep(1)
    pyautogui.click(x=1440, y=832) #OK
    progresso.update(1)
    time.sleep(24)
    progresso.update(1)
    pyautogui.click(x=1261, y=630)
    progresso.update(1)
    time.sleep(1)

