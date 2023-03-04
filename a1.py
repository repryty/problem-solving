# print("hi")
#주석

# score=40
# score=30
# print(score)

# 넓이=가로x세로
# width=1920
# height=1080
# print(width*height)
# for i in range(10):
#     print("A")
# a = 20
# b = 30
# print(a,b)
# a, b=b, a
# print(a,bool)

#초 =>분 초
# sec=2000
# min=sec//60
# sec2=sec%60
# print(min, "분 ", sec2, "초")

# money=10000
# price=150
# candy=money//price
# left=money%price
# print(candy, left)

# name=input("whats you name\n")
# print("you are",name)
# age=input("whats your age")
# print("you are ", age)
# score=40
# print("im 50")
# print("im %s"%50)
# print("im {}".format(50))
# print(f"im {score}".format(50))

# text="Helllo Worlld!!"
# print(text[3])

# inp=input("입력\n").split()
# for i in range(len(inp)):
#     print(inp[i][0], end="")

# score = 90
# if score >= 50:
#     print("a")
# else:
#     print("b")

# import turtle
# tt=turtle.Pen()
# while 1:
#     direction=input()
#     if direction =="왼":
#         tt.left(60)
#         tt.forward(100)
#     if direction =="오":
#         tt.left(-60)
#         tt.forward(100)
# inp=int(input())
# if inp%2!=0:
#     print("홀")
# else:
#     print("짝")

# inp=input()
# if len(inp)%2!=0:
#     print(inp[len(inp)//2])
# else:
#     print(inp[len(inp)//2-1], inp[len(inp)//2], end="", sep="")

# age =5
# tall=150
# if age >=8 or tall>=140:
#     print("can")
# else:
#     print("no")

#score = int(input("학점 "))
#star = float(input("평점 "))
#if score >= 140 and star >=2.0:
#    print("can")
#else:
#    print("no") 

# AppleQuality ="신선"
# ApplePrice = 500
# if AppleQuality =="신선":
#     if ApplePrice<1000:
#         print("10개를 구마한다")
#     else:
#         print("5개를 구매한다")
# else:
#     print("사지 않는다")

# user_list=["김김김", "박박박", "이이이", "고양이"]
# id=input("iD: ")

# if id in user_list:
#     #print("아이디가 있습니다")
#     password=input("PW: ")
#     if password=="12345678":
#         print("Access Granted")
#     else:
#         print("Access Denied")
# else:
#     print("Access Denied")

# import random
# answer = random.randint(1, 100)
# for i in range(10):
#     hoope=int(input("답:"))
#     if hoope==answer:
#         print("Correct!")
#         break
#     elif hoope>answer:
#         print("Down!")
#     elif hoope<answer:
#         print("Up!")
#     print(f"남은횟수:{10-i}")

# import random

# inp=input("가위바위보 ㄱㄱ\n")
# com=random.randint(1,3)
# if com == 1:
#     comp="가위"
# elif com == 2:
#     comp="바위"
# elif com == 3:
#     comp="보"
# print(comp)
# if inp=="가위":
#     if comp=="바위":
#         print("짐")
#     if comp=="보":
#         print("이김")
# elif inp=="바위":
#     if comp=="가위":
#         print("이김")
#     if comp=="보":
#         print("짐")
# elif inp=="보":
#     if comp=="가위":
#         print("짐")
#     if comp=="바위":
#         print("이김")
# elif inp==comp:
#     print("비김")

# Am Rhein, am rhein am deutschen rhein, wir alle wolle hüter sein.
# Lieb vaterland, magst ruhig sein, lieb vaterland, makst ruhig sein.
# Fest shutet und treu di wacht Die Wacht am Rhein, Fest shutet und treu die wacht die wacht am Rhein.
# Es braust ein ruf wie donnehal wie 

# for i in range(500):
#     print(f"Die Wacht am Rhein x{i+1}")
# # print("그러므로 성스러운 라인강은 결코 프랑스에 속하지 않을 것이다.")
# print("Damit wird der heilige Rhein niemals Frankreich gehören.")

# names=["Willhelm ii", "Otto von Bismark", "Paul von Clausewitz"]
# for i in names:
#     print(f"Hallo, {i}! Willkommen.")

# range(5) # 0, 1, 2, 3, 4
# range(1,6) # 1, 2, 3, 4, 5
# range(1,6,2) #1, 3, 5

# # FACTORiAL
# inp=int(input())
# end=1
# for i in range(1, inp+1):
#     end*=i
# print(end)

# # 1+2+3+4....+n
# inp=int(input())
# end=0
# for i in range(1, inp+1):
#     end+=i
# print(end)

# import turtle
# import random
# tt=turtle.Pen()
# # turtle.bgcolor("black")
# # tt.color("red")
# tt.speed(0)
# inp=int(input())
# for ii in range(6):
#     rd=random.randint(20, 80)
#     for i in range(inp):
#         tt.forward(200/inp*4)
#         tt.left(360/inp)
#     tt.right(60)
# turtle.mainloop()

