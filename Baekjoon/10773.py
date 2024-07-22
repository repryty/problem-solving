inp=[]
for _ in range(int(input())):
    inpu=int(input())
    if inpu==0: inp.pop()
    else: inp.append(inpu)
print(sum(inp))