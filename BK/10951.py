lines=[]
while input()!="":
    b=input()
    if b=="0 0":
        break
    else:
        lines.append(b)
for i in range(len(lines)):
    lines[i]=lines[i].split()
    print(int(lines[i][0])+int(lines[i][1]))