N=input()
inpN=list(map(int, input().split()))
M=input()
inpM=list(map(int, input().split()))

hashMap=dict()
for i in inpN:
    if hashMap.get(i)==None:
        hashMap[i]=1
for i in inpM:
    if hashMap.get(i)==None:
        print(0, end=" ")
    else: print(1, end=" ")