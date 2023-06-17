from tkinter import *
from tkinter.font import *

mouse = Tk()
mouse.title('¡Viva Espanã!')
font30 = Font(family="맑은 고딕", size=30)
font20 = Font(family="맑은 고딕", size=20)
posX = Label(mouse, text = '마우스 X:', font=font20)
posX.pack()
posY = Label(mouse, text = '마우스 Y:', font=font20)
posY.pack()
mouse.geometry("1920x1080")

def check(event):
    # print(event)
    # print(event.char, end="")
    posX["text"] = "마우스 X: " +str(event.x)
    posY["text"] = "마우스 Y: " +str(event.y)
    if event.num==1:
        print("좌클릭 감지")
    elif event.num==2:
        print("휠클릭 감지")
    elif event.num==3:
        print("우클릭 감지")
    
mouse.bind("<Button-1>", check) #마우스 왼 
mouse.bind("<Button-2>", check) #마우스 휠
mouse.bind("<Button-3>", check) #마우스 우

mouse.mainloop() 