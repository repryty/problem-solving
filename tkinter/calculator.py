from tkinter import *
from tkinter.font import *

cal = Tk()
cal.title("GLaDOS Calculator")
font30 = Font(family="맑은 고딕", size=30)
font20 = Font(family="맑은 고딕", size=20)

ent1=Entry(cal, justify=RIGHT, font=font30)
ent1.grid(row=0, column=0, columnspan=5)
ent2 = Entry(cal, width=1)
ent2.grid(row = 5, column = 0)

buttons=[
    '7', '8', '9', '+', 'C',
    '4', '5', '6', '-', ' ',
    '1', '2', '3', 'X', ' ',
    '.', '0', '=', '/', ' '
]
오류="오오오류우우"
def click(key):
    if key=="=":
        try:
            end=str(eval(ent1.get()))
            ent1.delete(0, END)
            ent1.insert(END, end)
        except:
            ent1.delete(0, END)
            ent1.insert(END, "입력 오류")
    elif key=="C":
        ent1.delete(0, END)
    elif key=="X":
        ent1.insert(END, "*")
    else:
        ent1.insert(END, key) 
def check(e):
    # print(e.keysym)
    if e.char in buttons or e.keysym=="BackSpace" or e.keysym=="Delete" or e.keysym=="Return":
        if e.keysym=="BackSpace" or e.keysym=="Delete":
            ent1.delete(len(ent1.get())-1)
        elif e.keysym=="Return" or e.keysym=="equal":
            try:
                end=str(eval(ent1.get()))
                ent1.delete(0, END)
                ent1.insert(END, end)
            except:
                ent1.delete(0, END)
                ent1.insert(END, "입력 오류")
        elif e.keysym=="C":
            ent1.delete(0, END)
        else:
            ent1.insert(END, e.char)

x = 0
for i in buttons:
    cmd = lambda y=i: click(y)
    btn=Button(cal, text=i, command=cmd, font=font30)
    btn.grid(row=x//5+1, column=x%5)
    x+=1 

cal.bind("<Key>", check)

cal.mainloop()