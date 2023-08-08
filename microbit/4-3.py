from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    if pin1.read_digital()==0:
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)