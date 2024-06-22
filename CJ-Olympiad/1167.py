"""
grid1 = [0 for i in range(10)]

for i in range(10):
    grid1[i] = input().split()


def defire(a, b):
    global grid1

    try:
        grid1[a - 1][b] = grid1[a - 1][b].replace("0", "9")
        if grid1[a - 1][b] == "1" or grid1[a - 1][b] == "2":
            grid1[a][b] = grid1[a][b].replace("1", "3").replace("2", "4")
            defire(a - 1, b)

        grid1[a + 1][b] = grid1[a + 1][b].replace("0", "9")
        if grid1[a + 1][b] == "1" or grid1[a + 1][b] == "2":
            grid1[a][b] = grid1[a][b].replace("1", "3").replace("2", "4")
            defire(a + 1, b)

        grid1[a][b + 1] = grid1[a][b + 1].replace("0", "9")
        if grid1[a][b + 1] == "1" or grid1[a][b + 1] == "2":
            grid1[a][b] = grid1[a][b].replace("1", "3").replace("2", "4")
            defire(a, b + 1)

        grid1[a][b - 1] = grid1[a][b - 1].replace("0", "9")
        if grid1[a][b - 1] == "1" or grid1[a][b - 1] == "2":
            grid1[a][b] = grid1[a][b].replace("1", "3").replace("2", "4")
            defire(a, b - 1)
    except:
        pass


# if a == 0 and b == 0:
#     if grid1[0][0] == "1":
#         grid1[1][0] == grid1[1][0].replace("0", "9")
#         grid1[0][1] == grid1[0][1].replace("0", "9")


for i in range(10):
    for j in range(10):
        if grid1[i][j] == "1":
            defire(i, j)

for i in range(10):
    for j in range(10):
        grid1[i][j] = grid1[i][j].replace("3", "1").replace("4", "2")

# print("\n")
for i in range(10):
    print(*grid1[i])
"""


grid1 = [0 for i in range(10)]

for i in range(10):
    grid1[i] = input().split()
