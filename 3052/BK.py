lines=[]
for i in range(10):
    lines.append(input())

nl=[]
for i in range(10):
    nl.append(int(lines[i])%42)
nl=list(set(nl))

print(len(nl))