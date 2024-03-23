N, M=list(map(int, input().split()))
inpN=[]
inpM=[]
for i in range(N):
    inpN.append(input())
for i in range(M):
    inpM.append(input())

hashMap=dict()
for i in inpN:
    if hashMap.get(i)==None:
        hashMap[i]=1
    else:
        hashMap[i]+=1
for i in inpM:
    if hashMap.get(i)==None:
        hashMap[i]=1
    else:
        hashMap[i]+=1
end=0
end2=[]
sortedHashMap=dict(sorted(hashMap.items()))
for i in sortedHashMap:
    if sortedHashMap[i]==2:
        end+=1
        end2.append(i)
    
print(end)
print("\n".join(end2))