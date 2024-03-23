N=int(input())
hashMap=dict()
for i in range(N):
    inpu=input()
    if hashMap.get(inpu)==None:
        hashMap[inpu]=1
    else:
        hashMap[inpu]+=1
maxHashMap=dict(sorted(hashMap.items(), key=lambda x:(x[1], x[0]), reverse=True))
