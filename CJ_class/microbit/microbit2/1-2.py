# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    for i in range(5):
        for ii in range(5):
            display.set_pixel(ii, i, 9)
        sleep(1000)
    for i in range(5):
        for ii in range(5):
            display.set_pixel(ii, i, 0)
        sleep(1000)
