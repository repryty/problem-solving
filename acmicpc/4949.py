
while True:
    succed=True
    stack1=[]
    inp=input()
    if inp==".":
        break
    for i in inp:
        if i=="(":
            stack1.append(1)
        elif i==")":
            if len(stack1)==0 or stack1[-1]!=1:
                print("no")
                succed=False
                break
            stack1.pop()
        elif i=="[":
            stack1.append(2)
        elif i=="]":
            if len(stack1)==0 or stack1[-1]!=2:
                print("no")
                succed=False
                break
            stack1.pop()
    # print(stack1)
    if len(stack1)==0 and len(stack1)==0 and succed:
        print("yes")
    elif succed:
        print("no")