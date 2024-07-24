inp=[]
for i in range(int(input())):
    inp.append([int(i) for i in input().split()])
inp.sort(key=lambda x: (x[1], x[0]))
print("\n".join(map(lambda x: " ".join(map(str, x)), inp)))