inp=input().lower()
list1=[0 for i in range(26)]
for i in range(len(inp)):
    for ii in range(26):
        if inp[i]==chr(97+ii):
            list1[ii]+=1
list2=sorted(list1, reverse=True)
# print(list2)
if list2[0]==list2[1]:
    print("?")
else:
    print(chr(list1.index(max(list1))+65))