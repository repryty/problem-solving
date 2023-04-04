from tkinter import * #tkinter.뭐시기 안쓰고 각자 가져오기
from tkinter.font import *

### HTML은 위대하고 CSS와 JS는 그의 사도이다 HTML은 위대하고 CSS와 JS는 그의 사도이다 ###

window = Tk()
font1=Font(family="나눔스퀘어라운드 Regular", size=30)
font2=Font(family="궁서체")
a=0

def click1():
    global a
    b1["text"] = "실패"
    b1["command"] = ""
    a+=1
    if a==2:
        text["text"] = "확인중"
def click2():
    global a
    b2["text"] = "실패"
    b2["command"] = ""
    a+=1
    if a==2:
        text["text"] = "확인중"

text = Label(window, text="안녕하세요", font=font1)
text.pack(padx=20, pady=20) 

b1=Button(window, text="확인", command=click1, font=font2)
b1.pack(side=LEFT, padx=20, pady=20)
b2=Button(window, text="거절", command=click2, font=font2)
b2.pack(side=RIGHT, padx=20, pady=20)
    

window.mainloop()

# pip install pyinstaller