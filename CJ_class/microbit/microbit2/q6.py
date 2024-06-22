from microbit import *
display.clear()
a=0
b=0

while True:
    # if pin1.read_digital():
    #     sleep(50)
    #     if a==0: 
    #         b+=1
    #     a=1
    # else: 
    #     if a==1:
    #         a=0
    if pin1.read_digital()!=0:
        sleep(50)
        # b+=1
        if pin1.read_digital()==0:
            b+=1
    print(b)