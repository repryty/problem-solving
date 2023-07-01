from tkinter import *

win = Tk()
win.title('NEWS HUB')

def check():
    print("a")

title = Label(win, text = 'News Hub')
title.grid(row = 0, column = 0, columnspan=4)
how = Entry(win, width=4)
how.grid(row = 0, column = 5)
for i in range(5):
    num = Label(win, text = str(i+1))
    num.grid(row = i+1, column = 0)
    ent = Entry(win)
    ent.grid(row = i+1, column = 1, columnspan=3)
    btn = Button(win, text = '확인', command = check)
    btn.grid(row = i+1, column = 5)
    

win.mainloop()