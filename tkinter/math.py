from tkinter import *
from tkinter.font import *
from tkinter.colorchooser import *

w = Tk()
w.title("Math.")

def mathh():
    try:
        end["text"]=str(eval(en1.get()))
    except:
        pass

font1=Font(family="맑은 고딕")

label1=Label(w, text="계산기", font=font1, pady=30)
label1.pack()



frame1=Frame(w, padx=10, pady=10)
en1=Entry(frame1, font=font1)
en1.pack(side=LEFT)
btn1=Button(frame1, text="계산하기", command=mathh, font=font1, fg="black", bg="white")
btn1.pack(side=RIGHT)
frame1.pack()

# color=askcolor()
# print(color)

# btn1['fg']=color[1]

end=Label(w, text="결과", font=font1)
end.pack()

photo = PhotoImage(file="orange.png")
lbp=Label(w, image=photo)
# lbp.photo=photo
lbp.pack()

w.mainloop()

# from tkinter import *
# from tkinter.font import *

# 계 = Tk()
# def 계산():
#     try:
#         결과["text"] = "결과: " + str(eval(엔1.get()))
#     except:
#         pass
# 계.title('계산기 made by 000')
# 폰트30 = Font(family="나눔스퀘어라운드", size=30)
# 폰트20 = Font(family="나눔스퀘어라운드", size=20)
# 레1 = Label(계, text = '계산기', font=폰트30, pady=30)
# 레1.pack()
# 프 = Frame(계, padx=10, pady=10)
# 엔1 = Entry(프, font=폰트30)
# 엔1.pack(side=LEFT)
# 버1 = Button(프, text = '계산하기', command = 계산, font=폰트20)
# 버1.pack()
# 프.pack()
# 결과 = Label(계, text = '결과', font=폰트20, pady=20)
# 결과.pack()
# 계.mainloop()