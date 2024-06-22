input1=int(input())
inputs=[list(map(int, input().split())) for i in range(input1)]

def bridge(n,m):
    if n==1:
        return m
    else:
        for i in range(1, n+1):
            print(bridge(n-1, m-i))

print(bridge(inputs[0][0], inputs[0][1]))