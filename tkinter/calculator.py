from tkinter import *
from tkinter.font import *

cal = Tk()
cal.title("GLaDOS Calculator")
font30 = Font(family="맑은 고딕", size=30)
font20 = Font(family="맑은 고딕", size=20)

ent1=Entry(cal, justify=RIGHT, font=font30)
ent1.grid(row=0, column=0, columnspan=5)

buttons=[
    '7', '8', '9', '+', 'C',
    '4', '5', '6', '-', ' ',
    '1', '2', '3', 'X', ' ',
    '.', '0', '=', '/', ' '
]
x = 0
for i in buttons:
    cmd = lambda y=i: click(y)
    btn=Button(cal, text=i, command=cmd, font=font20)
    btn.grid(row=x//5+1, column=x%5)
    x+=1

cal.mainloop()