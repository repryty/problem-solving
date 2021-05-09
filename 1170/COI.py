inp=int(input())

a=[]
for i in range(inp):
    i+=1
    if inp%i==0:
        a.append(i)

print(a)