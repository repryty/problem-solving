from microbit import *
import random
display.clear()
pins=[pin1,pin2]


while True:
    rand=random.getrandbits(1)
    pins[0].write_digital(1)
    pins[1].write_digital(1)
    print("random: ", rand)
    sleep(1000)
    pins[0].write_digital(0)
    pins[1].write_digital(0)
    pins[rand].write_digital(1)
    print(rand, "pin on")
    sleep(1000)
    if pin8.read_digital()==1 and rand==0:
        pins[0].write_digital(0)
        print("pin8 and rand 0")
        sleep(3000)
    elif pin12.read_digital()==1 and rand==1:
        pins[1].write_digital(0)
        print("pin12 and rand 1")
        sleep(3000)
    else:
        for i in range(5):
            pins[0].write_digital(1)
            pins[1].write_digital(1)
            sleep(100)
            pins[0].write_digital(0)
            pins[1].write_digital(0)
            sleep(100)
        sleep(1000)