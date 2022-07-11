import eel
import time 
from ahk import AHK
import keyboard
from socket import *
from time import ctime
from threading import Thread
ahk = AHK()
 
@eel.expose
def pog():
    for _ in range(48):
        ahk.click(1076, 375)
        time.sleep(0.3)
        ahk.click(983, 391)
        time.sleep(0.5)
        ahk.click(690, 459)
        time.sleep(0.5)
        ahk.click(693, 559)
        time.sleep(0.5)
        ahk.click(693, 559)
        time.sleep(0.5)
        ahk.click(693, 559)
        time.sleep(2)
        ahk.key_press('BS')
        time.sleep(1)
        ahk.key_press('0')
        ahk.click(888, 642)
   

eel.init("web")
eel.start("main.html", size=(900,700), port=8080)
 

