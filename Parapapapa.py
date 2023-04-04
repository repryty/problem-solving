import matplotlib.pyplot as plt
size=(['19.7', '19.6', '13', '8', '8', '8', '23']) #비율 설정
label= ['화웨이', '삼성', '애플', '오포', '샤오미', '비보', '기타'] #기업명 입력
color=['red', 'royalblue', 'gray', 'g', 'orange', 'skyblue', 'yellow'] #색 설정
plt.rc('font', family='Malgun Gothic') #폰트 설정
plt.title("스마트폰 점유율(2020년 5월)") #제목 설정
plt.pie(size, labels=label, colors=color, autopct='%.1f%%', 
explode=(0.09, 0.072, 0.05, 0.025, 0, 0, 0.06)) #파이그래프 만들기
plt.axis('equal')
# plt.figure(dpi=300)
plt.show()
plt.style.use('ggplot')
plt.barh(label, [19.7, 19.6, 13, 8, 8, 8, 23], color=color)#평범한 바그래프
plt.show()