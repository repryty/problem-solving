inp=int(input())
hashMap=dict()
manList=[]
for i in range(inp):
    inpu=input().split()
    manList.append(inpu[0])
    if inpu[1]=="enter":
        hashMap[inpu[0]]=1
    else:
        hashMap[inpu[0]]=0
end=[]
for i in list(set(manList)):
    if hashMap[i]==1:
        end.append(i)
end.sort(reverse=True)
print("\n".join(end))