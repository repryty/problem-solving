import requests
from bs4 import BeautifulSoup


keyword=input()

default="https://search.naver.com/search.naver?where=view&sm=tab_jum&query="+keyword

r=requests.get(default) #95.375 VENI VIDI VICI

bs=BeautifulSoup(r.text, "html.parser")
# print(bs)
# res=bs.find_all("a", class_="total_tit")
res=bs.select("a.total_tit") # best way to use the parser, but it need CSS exprience.
# print(res)
for i, item in enumerate(res, 1):
    print(str(i)+". "+item.text)  #+", "+item.herf
# for i in range(1, 21):
#     print("for i in range(10):")
#     for ii in range(i): print("    ", end="") 