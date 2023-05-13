from tkinter import *

grid=Tk()
grid.title("How to make GRID")

lab1=Label(grid, text="첫번째")
lab1.grid(row=0, column=0)
ent1=Entry(grid)
ent1.grid(row=0, column=1)
lab2=Label(grid, text="두번째")
lab2.grid(row=1, column=0)
ent2=Entry(grid)
ent2.grid(row=1, column=1)
lab3=Label(grid, text="세번째")
lab3.grid(row=2, column=0)
ent3=Entry(grid)
ent3.grid(row=2, column=1)
lab4=Label(grid, text="네번째")
lab4.grid(row=3, column=0)
ent4=Entry(grid)
ent4.grid(row=3, column=1)


grid.mainloop()