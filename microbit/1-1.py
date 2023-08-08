# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    for i in range(5):
        display.set_pixel(i, i, 9)
        display.set_pixel(4 - i, i, 9)
    sleep(1000)
    for i in range(5):
        display.set_pixel(i, i, 0)
        display.set_pixel(4 - i, i, 0)
    sleep(1000)
