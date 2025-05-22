a, b, c=map(int, input().split())
getmon=a
v=0
if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))
    #print(v+1)