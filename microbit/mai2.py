from microbit import *

display.clear()

servo=pin1
servo_period=20
degree0=int(1024/servo_period*0.6)
degree90=int(1024/servo_period*1.5)
degree180=int(1024/servo_period*2.5)

servo.set_analog_period(servo_period)
servo.write_analog(degree0)

while True:
    servo.write_analog(degree0)
    display.show("0")
    sleep(1000)
    servo.write_analog(degree90)
    display.show("9")
    sleep(1000)
    servo.write_analog(degree180)
    display.show("1")
    sleep(1000)