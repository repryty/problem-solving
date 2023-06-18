inp = list(map(int, input().split()))

a=2147483648

for i in range(len(inp)):
    if a>inp[i]:
        a=inp[i]
print(a)