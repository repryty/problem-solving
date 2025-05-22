N = int(input())
metrix = [["0" for _ in range(N)] for _ in range(N)]
for i in range(N):
    inp = [int(i) for i in input().split()]
    u, k, nodes = inp[0], inp[1], inp[2:]
    for i in nodes:
        metrix[u-1][i-1] = "1"
for i in range(N):
    print(" ".join(metrix[i]))