"""from random import randint

answer= randint(1,100)

#10번의 기회를 주는법
#while => 10번반복 
trying = 0
while trying<10:
    trying+=1
    predict=int(input("답: "))
    #답과 추측을 비교
    #답과 추측이 높은지 낮은지 같은지

    if answer>predict:
        print("UP!")
    elif answer==predict:
        break
    elif answer<predict:
        print("DOWN!")
#10번의 시도에도 못맞춘 경우, 답을 맞춘 경우
if answer==predict:
    print("정답!")
    print(f"시도횟수: {trying}")
else:
    print("실패")
    print(f"정답: {answer}")"""

"""### 중첩 반복문
for y in range(5): #줄 만들기
    for x in range(11): #별만들기
        print("*", end="")
print() #줄바꿈"""

"""word="apple"
for letter in word:
    print(letter, end=' ')"""

#문자의 자음 모음 개수 세기

"""원본=input("입력: ")
a=원본.lower() #영어 대문자 => 소문자
자음=0
모음=0
if len(a)>0 and a.isalpha() > 0:
    #소원의 문자갯수가 0보다 크고 소원에 알파벳이 0보다 크게 있다면
    for i in a:
        if i in "aeiou":
            모음+=1
        else:
            자음+=1

print(f"모음의 갯수: {모음}\n자음의 갯수: {자음}")"""

"""inp=input("입력: ")
end=""
#계좌번호에서 '-'빼기

for i in inp: #원본에서 한글짜씩 빼오기
    if i !="-": #-인지 아닌지 확인
        end+=i #최종에 더하기
print(end)"""

"""import function_practice

function_practice.hello()

function_practice.hallo()

function_practice.hola("kim", "jung")

print(function_practice.plus(1,2))"""

"""import function_practice
from random import randint

print(function_practice.is_prime(100))

while True:
    a=randint(1, 100)
    if function_practice.is_prime(a):
        print(a,"소수")
        break
    else:
        print(a,"소수가 아님")

print(function_practice.password(100000))"""

"""import turtle as tt

def right():
    tt.setheading(0)
    tt.forward(100)
def up():
    tt.setheading(90)
    tt.forward(100)
def left():
    tt.setheading(180)
    tt.forward(100)
def down():
    tt.setheading(270)
    tt.forward(100)
def delete():
    tt.clear()
    tt.penup()
    tt.goto(0,0)
    tt.pendown()
def pu():
    tt.penup()
def pd():
    tt.pendown()

tt.shape("turtle")

tt.onkeypress(right, "d")
tt.onkeypress(left, "a")
tt.onkeypress(up, "w")
tt.onkeypress(down, "s")
tt.onkeypress(delete, "Delete")
tt.onkeypress(pu, "q")
tt.onkeypress(pd, "e")

tt.listen()
tt.mainloop()
"""

##지역변수와 전역변수
##Local and Global
"""
def fruit():
    global a
    a="I ♥ APPLE"
    print(a)
fruit()
print(a)"""

"""def sub():
    return 1, 2, 3
a, b, c=sub()
print(a, b, c)"""

## 삼항 연산자

"""a=3
b=1 if a == 5 else 2
print(a, b)"""

## 람다 ##

"""sum = lambda x,y: x+y
print(sum(10,20))"""

#### 리스트 ####

"""scores = []
for i in range(3):
    scores.append(int(input("입력: ")))

print(scores)"""
## 50 60 70 80 90 100
#>>>> 중요 <<<< scores=list(map(int, input().split())) #map=>모두 바꿔주기
#print(scores)

# print(list("Katzen Reich"))

import turtle as tt
from random import randint
# color=["red", "blue", "pink", "yellow", "red", "blue", "yellow", "red", "blue", "yellow"]
# tt.shape("circle")
# length=50
# angle=360/8
# tt.width(5)
# for i in range(8):
#     tt.color(color[randint(0,9)])
#     tt.forward(length)
#     tt.right(angle)
# tt.mainloop()

color=["red", "blue","pink", "yellow"]
name=["k", "r", "b", "n"]
tt.bgcolor("black")

for i in range(4): #0-3
    name[i] = tt.Turtle()
    name[i].color(color[i])
    name[i].penup()
    tt.speed(0)
    name[i].goto(-300, i*80-100)
    name[i].pendown()
    tt.speed(10)
    for j in range(20):
        name[i].forward(randint(5, 25))
tt.mainloop()