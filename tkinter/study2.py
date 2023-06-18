from tkinter import *
from tkinter.font import *

tkc=Tk()
font1=Font(family="맑은 고딕", size=30)

def prac():
    print(entry1.get())
    label1["text"]=eval(entry1.get())

f=Frame(tkc)
entry1 = Entry(f, font=font1)
entry1.pack()
btn1=Button(f, text="연습", command=prac)
btn1.pack()
f.pack()
label1=Label(f, font=font1)
label1.pack()
f.mainloop()
