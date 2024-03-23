N,M=list(map(int,input().split()))
hashMap=dict()
for i in range(N):
    inp=input()
    hashMap[inp]=1
end=0
for i in range(M):
    if hashMap.get(input())!=None:
        end+=1

print(end)