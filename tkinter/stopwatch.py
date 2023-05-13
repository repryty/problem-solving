from tkinter import *
from tkinter.font import *

window = Tk()
window.title("STOPWATCH")
fonts = Font(family="맑은 고딕", size= 20)
fonts2 = Font(family="맑은 고딕", size= 50)

flag = False
def start():
    global flag
    flag = True

def stop():
    global flag
    flag = False

h, m, s, ms=0, 0, 0, 0

def startTimer():
    global h, m,s,ms, flag
    if flag:
        ms += 1
    if ms>=100:
        ms=0
        s+=1
    if s>=60:
        s=0
        m+=1
    if h>=60:
        m=0
        h+=1
    time["text"] = f"{h:02d}:{m:02d}:{s:02d};{ms:02d}"
    window.after(3, startTimer)

time=Label(window, text= '00:00:00;000', font=fonts2)
time.grid(row=0, column=0)
time1=Button(window, text='시작', command=start, font=fonts, width=25, bg='yellow')
time1.grid(row=1,column=0)
time2=Button(window, text='정지', command=stop, font=fonts, width=25, bg='yellow')
time2.grid(row=2, column=0)
startTimer()
window.mainloop()