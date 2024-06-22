input()
A=list(map(int, input().split()))
B=list(map(int, input().split()))

AmB=dict()
for i in A:
    AmB[i]=1
for i in B:
    if AmB.get(i)!=None:
        AmB.pop(i)
ApB=dict()
for i in B:
    ApB[i]=1
for i in A:
    if ApB.get(i)!=None:
        ApB.pop(i)
print(len(AmB)+len(ApB))
