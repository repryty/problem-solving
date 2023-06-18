from tkinter import *
from tkinter.font import *

grid=Tk()
grid.title("How to make GRID")
font1=Font(family="맑은 고딕", size=20)

lab1=Label(grid, text="첫번째", font=font1)
lab1.grid(row=0, column=0)
ent1=Entry(grid, font=font1)
ent1.grid(row=0, column=1)
lab2=Label(grid, text="두번째", font=font1)
lab2.grid(row=1, column=0)
ent2=Entry(grid, font=font1)
ent2.grid(row=1, column=1)
lab3=Label(grid, text="세번째", font=font1)
lab3.grid(row=2, column=0)
ent3=Entry(grid, font=font1)
ent3.grid(row=2, column=1)
lab4=Label(grid, text="네번째", font=font1)
lab4.grid(row=3, column=0)
ent4=Entry(grid, font=font1)
ent4.grid(row=3, column=1)

def get():
    print(f"Getting First Value..... {ent1.get()}")
    print(f"Getting Second Value..... {ent2 .get()}")
    print(f"Getting Third Value..... {ent3.get()}") 
    print(f"Getting Quad Value..... {ent4.get()}") 
    lab5["text"]=str(int(ent1.get())+int(ent2.get())+int(ent3.get())+int(ent4.get()))


Button(grid, text="가져오기", font=font1, bg="white", command=get).grid(row=4, column=0)
Button(grid, text="끝내기", font=font1, bg="white", command=grid.quit).grid(row=4, column=1)

lab5=Label(grid, text='', font=font1)
lab5.grid(row=5, column=0)



grid.mainloop()