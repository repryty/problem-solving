lines=[]
for i in range(2):
    lines.append(input())
how, man=lines
man=man.split()
plus=0
for i in range(int(how)):
    plus+=int(man[i])
print(plus/int(how))