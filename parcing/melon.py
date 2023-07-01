import requests
from bs4 import BeautifulSoup

web="https://www.melon.com/chart/index.htm"
hdr={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Whale/3.21.192.18 Safari/537.36"
}
req=requests.get(web, headers=hdr)
soup=BeautifulSoup(req.text, "html.parser")
# print(req.text)

res=soup.select(".ellipsis.rank01 a")
res2=soup.select(".ellipsis.rank02 a")
for i, item in enumerate(res, 1):
    print(str(i)+"위: " +item.text+" / "+res2[i].text)

dic1={} 
for i in range(100):
    if res2[i].text in dic1:
        dic1[res2[i].text]+=1
    else:
        dic1[res2[i].text]=0
# dic1.sort()
print("====가수 일람====")
# print(dic1.items())
d2 = sorted(dic1.items(), key=lambda x: x[1], reverse=True)
# print(d2, sep="\n", end="")
for i in range(len(d2)):
    print(str(i+1)+"위, "+d2[i][0]+", "+str(d2[i][1])+"곡 등재")