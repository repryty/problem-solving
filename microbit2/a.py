# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    inp = input("what number? ")

    if inp == "R":
        pin1.write_digital(1)
        pin2.write_digital(0)
        pin8.write_digital(0)
        print("Red is on!")
        sleep(1000)
        pin1.write_digital(0)
    elif inp == "Y":
        pin1.write_digital(0)
        pin2.write_digital(1)
        pin8.write_digital(0)
        print("Yellow is on!")
        sleep(1000)
        pin2.write_digital(0)
    elif inp == "B":
        pin1.write_digital(0)
        pin2.write_digital(0)
        pin8.write_digital(1)
        print("Blue is on!")
        sleep(1000)
        pin8.write_digital(0)
    else:
        print("Wrong Input!")
