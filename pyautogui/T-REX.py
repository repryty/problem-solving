from PIL import ImageGrab, ImageOps
import pyautogui as g
import time
from numpy import *
# rex 104 412, leftup 145 406, rightdown 213 468
startingMousePosition=[481, 404]
TRexPosition=[104, 410]

track=[TRexPosition[0]+100, TRexPosition[1], TRexPosition[0]+150, TRexPosition[1]+30]
g.click(startingMousePosition)

while True:
    screen=ImageGrab.grab(track)
    grayscaled=ImageOps.grayscale(screen)
    combined=array(grayscaled.getcolors()).sum()
    print(combined)
    if combined!=1755 and combined!=1500:
        g.press("space")