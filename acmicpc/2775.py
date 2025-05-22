for i in range(int(input())):
    k = int(input())
    n = int(input())

    stairs=[[0 for _ in range(n)] for _ in range(k+1)]
    stairs[0]=[ii for ii in range(1, n+1)]

    for ii in range(1, k+1):
        for iii in range(n):
            stairs[ii][iii] = sum(stairs[ii-1][:iii+1])
    print(stairs[k][n-1])