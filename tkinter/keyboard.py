from tkinter import *
from tkinter.font import *

keyboard = Tk()
keyboard.title('Name This Window')
font30 = Font(family="맑은 고딕", size=30)
font20 = Font(family="맑은 고딕", size=20)
whatkey = Label(keyboard, text = '입력한 키는', font=font20)
whatkey.pack()

keysym = Label(keyboard, text = '입력한 키의 sym은', font=font20)
keysym.pack()

def check(event):
    # print(event)
    # print(event.char, end="")
    whatkey["text"] = "입력한 키는 " +event.char
    keysym["text"] = "입력한 키의 sym은 " +event.keysym
keyboard.bind("<Key>", check)

keyboard.mainloop()