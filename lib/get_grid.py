M, N, K = [int(i) for i in input().split()]

grid = [["0" for _ in range(N)] for _ in range(M)]
for i in range(K):
    x, y = [int(i) for i in input().split()]
    grid[x][y] = "1"

print("\n".join([" ".join(grid[i]) for i in range(N)]))