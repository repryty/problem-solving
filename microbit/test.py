# Imports go at the top
from microbit import *

pins=[pin1, pin2, pin8, pin12, pin13, pin14, pin15]
presets=[[0,0,0,0,0,1,0],[1,0,0,1,1,1,1],[0,0,1,0,0,0,1],[0,0,0,0,1,0,1],[1,0,0,1,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]
# Code in a 'while True:' loop repeats forever
while True:
    display.clear()
    for ii in range(10):
        for i in range(7):
            pins[i].write_digital(presets[ii][i])
        sleep(300)
    for ii in range(8, 0, -1):
        for i in range(7):
            pins[i].write_digital(presets[ii][i])
        sleep(300)