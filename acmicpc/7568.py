n = int(input())
weight, tall, end=[[0 for _ in range(n)] for i in range(3)]
for i in range(n):
    weight[i], tall[i] = map(int, input().split())
for i in range(n):
    for ii in range(n):
        if weight[ii]>weight[i] and tall[ii]>tall[i]: end[i]+=1
print(" ".join(map(lambda x: str(x+1), end)))