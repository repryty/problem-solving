from microbit import *
import random
display.clear()
pins=[pin16, pin2, pin8, pin12, pin13, pin14, pin15]
presets=[[0,0,0,0,0,1,0],[1,0,0,1,1,1,1],[0,0,1,0,0,0,1],[0,0,0,0,1,0,1],[1,0,0,1,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]
n=0
b=0
didit=0

while True:
    poten = pin1.read_analog() #0~1000
    if poten <200:
        n=1
    elif poten<400:
        n=2
    elif poten<600:
        n=3
    elif poten<800:
        n=4
    else:
        n=5

    for i in range(7):
        pins[i].write_digital(presets[n][i])