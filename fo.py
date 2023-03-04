import random
table=list(range(6))
for i in range(6000000):
    rd=random.randint(1, 6)
    table[rd-1]+=1
    print(table, end="")
    a=0
    for i in range(6):
        a+=table[i]
    print("평균:",a//6, "현재 수:", rd)