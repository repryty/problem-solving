from microbit import *

# 마이크로비트 <-> PC 시리얼 통신 속도 설정(1초에 9600bit)
uart.init(baudrate=9600) 

while True:
    data = uart.read() # 시리얼 통신으로 입력 받은 정보를 data 변수에 입력받기
    if data == b'r':   # 입력 받은 정보가 b'1'(클래스명이 '1' -> 마스크 O)이라면
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif data == b'y': # 입력 받은 정보가 b'0'(클래스명이 '0' -> 마스크 X)이라면
        pin1.write_digital(0)
        pin2.write_digital(1)