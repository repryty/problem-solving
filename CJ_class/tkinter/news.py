from tkinter import *
from tkinter.font import *

window = Tk()
window.title("자동-뉴스수집 프로그램")
fonts = Font(family="맑은 고딕", size= 30)
fonts2 = Font(family="맑은 고딕", size= 50)

time=Label(window, text= '현재시간: 2023.02.15-15:11:44', font=fonts2)
time.grid(row=0, column=1, columnspan=5)
time2=Entry(window, width=3, font=fonts2) 
time2.grid(row=0, column=6)
time2.insert(END, "1분")
for i in range(1, 6):
    label1=Button(window, text=str(i), font=fonts)
    label1.grid(row=i, column=0)
    inp1=Entry(window, font=fonts, width=40)
    inp1.grid(row=i,column=1,columnspan=5)
    btn1=Button(window,text="LINK", font=fonts)
    btn1.grid(row=i,column=6)


window.mainloop()