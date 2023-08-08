# Imports go at the top
from microbit import *
r=pin8
g=pin1
b=pin2

# Code in a 'while True:' loop repeats forever
while True:
    display.clear()
    inp=input("색입력")
    if inp=="r":
        r.write_digital(0)
        g.write_digital(1)
        b.write_digital(1)
    if inp=="g":
        r.write_digital(1)
        g.write_digital(0)
        b.write_digital(1)
    if inp=="b":
        r.write_digital(1)
        g.write_digital(1)
        b.write_digital(0)
    if inp=="y":
        r.write_digital(0)
        g.write_digital(0)
        b.write_digital(1)
    if inp=="p":
        r.write_digital(1)
        g.write_digital(0)
        b.write_digital(0)
    if inp=="t":
        r.write_digital(1)
        g.write_digital(0)
        b.write_digital(0)