import pyautogui as g
import time
import pyperclip as pc
import random

# def access():
#     e=g.prompt("비밀번호", title="보안 확인중")
#     if e=="12304":
#         a=g.alert(text="보안문제 3개 발견됨", title="경고", button="확인")
#         b=g.confirm(text="삭제하시겠습니까?", title="자동 삭제", buttons=["확인", "취소"])
#         if b=="확인":
#             c=g.alert(text="삭제 성공", title="성공", button="확인")
#         else:
#             d=g.alert(text="보안 문제가 해결되지 않았습니다.", title="경고", button="확인")
#     else:
#         f=g.alert(text="접근 거부", title="경고", button="확인")
#         access()

# access()

# print(str(g.size()).replace("1920", "2560").replace("1080", "1600"))
# while True:
#     print(g.position())
#     time.sleep(0.1)
# g.click(16,1080)
# g.moveTo(393, 272)
# g.dragTo(393, 980,3, button="primary", mouseDownUp=True)
# g.scroll(-1000)

# for i in range(100): g.write("Hello, World!", interval=0.05)
# g.press("w",5, 0.1)# Hi, Myy 
# print(g.position())
# g.hotkey("Ctrl","C")
# g.click(1052, 563)
# g.hotkey("Ctrl","V")
# g.click(1052, 563)

# position=g.locateCenterOnScreen("windows.png")
# print("windwos:", position)
# g.click(position)
# time.sleep(2)
# position=g.locateCenterOnScreen("A.png")
# print("A:", position)
# g.click(position)
# time.sleep(2)
# position=g.locateCenterOnScreen("nien.png")
# print("ㄴ:", position)
# g.click(position)
# time.sleep(2)
# position=g.locateCenterOnScreen("whale.png")
# print("whale:", position)
# g.click(position)

# inp=input().replace("/", "s")
# for i in range(len(inp)):
#     position=g.locateCenterOnScreen(f"{inp[i]}.png")
#     print("pos:", position)
#     g.click(position)
#     time.sleep(0.4)

g.hotkey("win", "r")
time.sleep(0.7)
g.write("whale")
g.hotkey("enter")
time.sleep(3)

position=g.locateCenterOnScreen("ga.png")
if position!=None:
    g.hotkey("hangul")
g.write("youtube.com", interval=0.1)
g.hotkey("enter")
time.sleep(5)

for i in range(4): g.press("tab")
time.sleep(0.5)
pc.copy("프리드리히 대왕 척탄병 행진곡")
g.hotkey("Ctrl", "v")

g.press("space")    
time.sleep(1)
g.press("enter")
g.press("tab")
g.press("tab")
g.hotkey("shift","tab")
g.hotkey("shift","tab")
time.sleep(1)
g.press("enter")
time.sleep(3)
g.hotkey("ctrl", "t")
g.write("naver.com", interval=0.1)
g.press("enter")
time.sleep(2)
# position=g.locateCenterOnScreen("search.png")
# print("pos:", position)
# for i in range(5): g.click(position)
strings=["독일 제국", "청천백일만지홍기", "찰스 3세", "프로이센 왕국"][random.randint(0, 3)]
pc.copy(strings)
g.hotkey("Ctrl", "v")
g.press("enter")
for i in range(200):
    g.scroll(-100)