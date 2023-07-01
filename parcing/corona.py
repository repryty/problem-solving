import requests
from bs4 import BeautifulSoup
from tkinter import *

win=Tk()



r = requests.get("https://ncov.kdca.go.kr/")
soup=BeautifulSoup(r.text, "html.parser")
res=soup.select(".ds_table>tbody>tr>td>span")

for i, item in enumerate(res):
    if i==0: print("사망")
    elif i==1: print("재원 위중증")
    else: print("확진")
    print(item.text) 

la1=Label(win, text=res[2].text)
la1.pack()

    

win.mainloop()