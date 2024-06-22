from microbit import *

pins=[pin1, pin2, pin8, pin12, pin13, pin14, pin15]
presets=[[0,0,0,0,0,1,0],[1,0,0,1,1,1,1],[0,0,1,0,0,0,1],[0,0,0,0,1,0,1],[1,0,0,1,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]
# Code in a 'while True:' loop repeats forever
while True:
    display.clear()
    n1=int(input("1번수: "))
    n2=int(input("2번수: "))
    if n1>n2:
        n=n1-n2
    else:
        n=n2-n1


    for i in range(7):
        pins[i].write_digital(presets[n][i])