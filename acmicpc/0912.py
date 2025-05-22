N=int(input())

for i in range(N):
    inp=input()
    stack=[]
    end=""
    for ii in inp:
        if ii=="(":
            stack.append("(")
        elif ii==")" and len(stack)==0:
            end="NO"
            break
        else:
            stack.pop()
    if end!="NO":
        if len(stack)==0:
            print("YES")
        else:
            print("NO")
    else:
        print(end)