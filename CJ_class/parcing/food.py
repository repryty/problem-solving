import requests
from bs4 import BeautifulSoup 
import datetime
from tkinter import *
from tkcalendar import DateEntry

def food():
    날짜 = str(달력.get_date())
    날짜 = 날짜[0:4] + 날짜[5:7] + 날짜[8:]
    web="https://school.cbe.go.kr/chungil-m/M01030902/list?ymd="+when
    req=requests.get(web)
    soup=BeautifulSoup(req.text, "html.parser")
    res1=soup.select(".tch-lnc>ul>li")
    if res1 == []: print(f"{when}, 급식 정보 미확인")
    else: 
        for item in res1:
            print(item.text.split(" (")[0])

win=Tk()
frame=Frame(win)
cal=DateEntry(win)
cal.pack(side=LEFT)
btn=Button(frame, text="가져오기", command=food)
btn.pack()
frame.pack()

# when=""
# # when=input("며칠? YYYYMMDD or MMDD or Enter: ")
# if len(when)==4:
#     when="2023"+when
# elif when=="":
#     when =str(datetime.datetime.now())[:10].replace("-","")
# web="https://school.cbe.go.kr/chungil-m/M01030902/list?ymd="+when
# req=requests.get(web)
# soup=BeautifulSoup(req.text, "html.parser")
# res1=soup.select(".tch-lnc>ul>li")
# # a,b=[],[]
# if res1 == []: print(f"{when}, 급식 정보 미확인")
# else: 
#     for item in res1:
#         print(item.text.split(" (")[0])
# # print(a)

win.mainloop()