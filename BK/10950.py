lines=[]
how=int(input())
for i in range(how):
    lines.append(input())

for i in range(how):
    a, b=lines[i].split()
    print(int(a)+int(b))