import requests ## html 가져와줘!!
from bs4 import BeautifulSoup ## 분석해줘!!
from tkinter import *
from tkcalendar import DateEntry
윈 = Tk()
def 급식():
    날짜 = str(달력.get_date())
    날짜 = 날짜[0:4] + 날짜[5:7] + 날짜[8:]
    주소 = "https://school.cbe.go.kr/chungil-m/M01030902/list?ymd=" + 날짜
    r = requests.get(주소)
    soup = BeautifulSoup(r.text, "html.parser")
    메뉴 = soup.find("a", href="/chungil-m/M01030902/list?ymd=" + 날짜)
    try:
        메뉴 = 메뉴.find_all("li")
        식단 = ""
        for i in 메뉴:
            식단 = 식단 + i.text + "\n"
    except:
        식단 = "오늘은 급식이 없어요!!!"
        pass
    print(식단)
    레1["text"] = 식단

제목=Label(윈, text="충일중 급식")
제목.pack()
프레임 = Frame(윈)
달력 = DateEntry(프레임)
달력.pack(side = LEFT)
버1 = Button(프레임, text="가져오기", command=급식)
버1.pack()
프레임.pack()
레1 = Label(윈)
레1.pack()
윈.mainloop()
