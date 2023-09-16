from microbit import *
display.clear()

# 마이크로비트 <-> PC 시리얼 통신 속도 설정(1초에 9600bit)
uart.init(baudrate=115200) 

while True:
    data = uart.read() # 시리얼 통신으로 입력 받은 정보를 data 변수에 입력받기
    if data == b'1':   # 입력 받은 정보가 b'1'(클래스명이 '1' -> 마스크 O)이라면
       display.show(Image.HEART) 
    elif data == b'0': # 입력 받은 정보가 b'0'(클래스명이 '0' -> 마스크 X)이라면
       display.show(Image.NO)