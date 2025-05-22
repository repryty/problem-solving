N,M=list(map(int, input().split()))
inp=list(map(int, input().split()))
maxCard=0

for i in range(N-2): 
    for ii in range(i+1,N-1):
        for iii in range(ii+1,N):
            result=inp[i]+inp[ii]+inp[iii]
            if result>M:
                pass
            else:
                if maxCard<=result:
                    maxCard=result

print(maxCard)