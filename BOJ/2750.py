lines=[]
how=int(input())
for i in range(how):
    lines.append(int(input()))
end=sorted(lines)
end=map(str, end)
print("\n".join(end))