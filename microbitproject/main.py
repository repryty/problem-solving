from microbit import *
display.clear()
old_level=0
light_level=0
timer1=0
forcetemp=0
fan=0

while True:
    if button_a.was_pressed():
        temp=int(input("temp: "))
        forcetemp=1
    if button_b.was_pressed():
        forcetemp=0
    timer1+=1
    # print(timer1)
    # display.scroll(display.read_light_level()) #255
    if timer1==100:
        light_level=float(1600/(display.read_light_level()/20))
        CAmount=max([light_level-old_level, old_level-light_level])
        print(light_level, old_level, CAmount, end="")
        if (light_level)<=1023:
            print(" Played, it will take", (int(CAmount)*50)/2000, "seconds.", "temp:", temp)
            for i in range(int(CAmount)):
                if light_level-old_level<0:
                    pin8.write_analog(old_level-i)
                else:
                    pin8.write_analog(old_level+i)
                if old_level!=1023:
                    sleep(20)
            old_level=light_level
        else:
            print("")
            if old_level<1023:
                for i in range(int(1023-old_level)):
                    pin8.write_analog(old_level+i)
            if old_level>=1023:
                for i in range(int(old_level-1023)):
                    pin8.write_analog(old_level-i)
            old_level=1023
            # pin8.write_analog(light_level)
        timer1=0
    if forcetemp==0:
        temp=temperature()
    templevel = temp//(22/5)
    display.show(int(templevel))

    pin16.set_analog_period(20) 
    degree0 = int(1024 / 20 *0.6)
    degree90 = int(1024 / 20 *1.5)
    if templevel>7 and fan == 0:
        pin16.write_analog(degree90)
        fan=1
        sleep(500)
        pin16.write_analog(degree0)
    elif templevel<=7:
        pin16.write_analog(degree0)
        fan=0