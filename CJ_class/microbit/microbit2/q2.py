from microbit import *

pins=[pin1, pin2, pin8, pin12, pin13, pin14, pin15]
presets=[[0,0,0,0,0,1,0],[1,0,0,1,1,1,1],[0,0,1,0,0,0,1],[0,0,0,0,1,0,1],[1,0,0,1,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]
# Code in a 'while True:' loop repeats forever
while True:
    inp=int(input("입력받을수: "))
    en=[]
    for i in range(inp):
        en.append(int(input(str(i+1)+"번째 수 입력: ")))
    print("입력 받은 정수 목록: ")
    for i in range(inp):
        print(en[i], end=" ")
    print()
    iv=input("출력하고 싶은 메뉴(1: 최대, 2: 최소)") 
    if iv=="1":
        for i in range(7):
            pins[i].write_digital(presets[max(en)][i])
    else:
        for i in range(7):
            pins[i].write_digital(presets[min(en)][i])