from microbit import *
display.clear()

pins=[pin1, pin2, pin8, pin12, pin13, pin14, pin15]
presets=[[0,0,0,0,0,1,0],[1,0,0,1,1,1,1],[0,0,1,0,0,0,1],[0,0,0,0,1,0,1],[1,0,0,1,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]

uart.init(baudrate=9600) 
ii=0
# Code in a 'while True:' loop repeats forever
while True:
    data = uart.read()
    if data == b'1': 
        ii=1
        display.show(ii)
    elif data == b'2':
        ii=2
        display.show(ii)

    for i in range(7):
        pins[i].write_digital(presets[ii][i])

         