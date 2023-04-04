input()
ss=list(map(int, input().split()))
end=0
for i in range(len(ss)):
    if ss[i]%2==0 or ss[i]%3==0 or ss[i]%5==0 or ss[i]%7==0:
        end+=1
print(end)