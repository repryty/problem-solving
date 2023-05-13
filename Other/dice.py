how=int(input())
lines=[]
for i in range(how):
    lines.append(list(map(int, input().split())))
end=[0 for i in range(how)]
e=[1 for i in range(how)]
for i in range(how):
    for ii in range(1, 7):
        if str(lines[i]).count(str(ii))==2:
            if e[i]<2:
                e[i]=2
                end[i]=ii
        elif str(lines[i]).count(str(ii))==3:
            if e[i]<3:
                e[i]=3
                end[i]=ii
        else:
            if e[i]<1:
                e[i]=1
                end[i]=ii
r=max(e)
f=e.index(r)+1
if r==1:
    print(f*100)
elif r==2:
    print(1000+(f*100))
elif r==3:
    print(10000+(f*1000))