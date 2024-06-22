N=int(input())
cards=list(map(int, input().split()))
M=int(input())
cardsToFind=list(map(int, input().split()))

hashMap=dict()
for i in cards:
    if hashMap.get(i)==None:
        hashMap[i]=1
    else:
        hashMap[i]+=1
end=[]
for i in cardsToFind:
    if hashMap.get(i)==None:
        end.append("0")
    else:
        end.append(str(hashMap[i]))

print(" ".join(end))