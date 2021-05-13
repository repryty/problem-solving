lines=[]
for i in range(5):
    lines.append(input())
ipos=0
jpos=0
for i in range(5):
    if lines[i].find("1")!=-1:
        ipos=i
for i in range(5):
    j=lines[ipos].split()
    if j[1] == "1":
        jpos=i
print(ipos, jpos)

