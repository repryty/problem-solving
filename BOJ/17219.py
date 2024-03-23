N,M=list(map(int, input().split()))
hashMap=dict()
for i in range(N):
    inpu=input().split()
    hashMap[inpu[0]]=inpu[1]

for i in range(M):
    print(hashMap[input()])