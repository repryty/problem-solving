h,w=map(int, input().split())
panel=[[0 for i in range(w)] for i in range(h)]
howm=int(input())
sticks=[]
for i in range(howm):
    sticks.append(list(map(int, input().split())))
for i in range(howm):
    for ii in range(sticks[i][0]):
        if sticks[i][1]==0:
            panel[sticks[i][2]-1][sticks[i][3]-1+ii]=1
        if sticks[i][1]==1:
            panel[sticks[i][2]-1+ii][sticks[i][3]-1]=1
for i in range(h):
    print(" ".join(list(map(str, panel[i]))))