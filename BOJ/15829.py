L=int(input())
inp=input()
end=0

for i in range(L):
    end+=(ord(inp[i])-96)*(31**i)
print(end%1234567891)