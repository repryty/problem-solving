input1 = [list(input()) for i in range(4)]
success = False
for i in range(3):
    for j in range(3):
        a = 0
        b = 0
        if input1[i][j] == "#":
            a += 1  # [y][x]
        if input1[i + 1][j] == "#":
            a += 1  # [y][x]
        if input1[i][j + 1] == "#":
            a += 1  # [y][x]
        if input1[i + 1][j + 1] == "#":
            a += 1  # [y][x]
        if input1[i][j] == ".":
            b += 1  # [y][x]
        if input1[i + 1][j] == ".":
            b += 1  # [y][x]
        if input1[i][j + 1] == ".":
            b += 1  # [y][x]
        if input1[i + 1][j + 1] == ".":
            b += 1  # [y][x]
        if a > 2 or b > 2:
            success = True

if success:
    print("YES")
else:
    print("NO")
