N=int(input())

if N%5==0:
    print(N//5)
else:
    end=0
    while N>0:
        N-=3
        end+=1
        if N%5==0:
            print(end+N//5)
            break
        elif N==1 or N==2:
            print(-1)
            break
        elif N==0:
            print(end)
            break