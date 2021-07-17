#2차원 리스트 생성하기
arr=[list(map(int,input().split()))for i in range(19)]

a=int(input())#좌표 개수 입력받기

for i in range(a):
    x,y=map(int,input().split())#좌표 개수 a만큼 좌표 입력받기(x,y)

    for j in range(19):
        if(arr[j][y-1]==1): #arr[0][9], arr[1][9], arr[2][9]... 십자뒤집기 시작!(행)
            arr[j][y-1]=0
        else:
            arr[j][y-1]=1

        if(arr[x-1][j]==1):#arr[9][0]], arr[9][1], arr[9][2]... 십자뒤집기 시작!(열)
            arr[x-1][j]=0
        else:
            arr[x-1][j]=1
        
#결과 출력하기
for i in range(19) :
  for j in range(19) : 
    print(arr[i][j], end=' ')
  print()
