inp=int(input())
inpu=[input() for i in range(inp)]

len1=len(inpu[0])
end=""
for i in range(len1):
    a=""
    for ii in range(inp):
        if a!="" and a==inpu[ii][i]:
            