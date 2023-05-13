back=[]
for i in range(9):
    back.append(list(map(int, input().split())))
end=[0, 0, 0]
for i in range(9):
    for ii in range(9):
        if end[0]<int(back[i][ii]):
            end[0]=back[i][ii]
            end[1]=ii
            end[2]=i
print(end[0])
print(end[2]+1, end[1]+1)