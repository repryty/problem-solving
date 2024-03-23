inp=[]
for i in range(int(input())):
    inp.append(tuple(map(int, input().split())))

inp=list(sorted(inp, key=lambda x: (x[0], x[1])))

for i in inp:
    print(int(i[0]), int(i[1]))