N, k = [int(i) for i in input().split()]
inp=[]
for i in range(N):
    inp.insert(0, int(input()))
end=0
for i in inp:
    while True:
        k-=i
        if k<0: 
            k+=i
            break
        end+=1
print(end)