L = int(input())
table=[[0 for i in range(0-L, L+1)] for i in range(0-L, L+1)]

# print(table)
N = int(input())
howMuchGo,whereToGo=[0 for i in range(N)],[0 for i in range(N)]
for i in range(N):
    howMuchGo[i], whereToGo[i] = input().split()
    howMuchGo[i]=int(howMuchGo[i])

snakeAngle, snakePos=90, [L,L]
end=0

def forward(lr):
    global snakePos
    if lr==90:
        snakePos=[snakePos[0], snakePos[1]+1]
    elif lr==180:
        snakePos=[snakePos[0]+1, snakePos[1]]
    elif lr==270:
        snakePos=[snakePos[0], snakePos[1]-1]
    elif lr==0:
        snakePos=[snakePos[0]-1, snakePos[1]]

for i in range(N):
    if table[snakePos[0]][snakePos[1]]==1: break
    for ii in range(howMuchGo[i]):
        if table[snakePos[0]][snakePos[1]]!=1: table[snakePos[0]][snakePos[1]]=1
        else: break
        forward(snakeAngle)
        end+=1
    
    if whereToGo[i] == "L" and snakeAngle!=0:
        snakeAngle-=90
    elif whereToGo[i] == "L" and snakeAngle==0:
        snakeAngle=270
    elif whereToGo[i] == "R" and snakeAngle!=270:
        snakeAngle+=90
    elif whereToGo[i] == "R" and snakeAngle==270:
        snakeAngle=0

print(end)