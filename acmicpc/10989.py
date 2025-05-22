import sys
n=int(sys.stdin.readline())
inp = [0]*10001
for i in range(n):
    inp[int(sys.stdin.readline())]+=1
for i in range(10001):
    for ii in range(inp[i]):
        sys.stdout.write(str(i)+"\n")