# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    pin8.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(1)
    sleep(1000)
    pin8.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(1000)
    pin8.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(1000)