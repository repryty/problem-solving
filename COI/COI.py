inp=[]
for i in range(10):
    inp.append(input())

list1=[inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6], inp[7], inp[8], inp[9]]

for i in range(10):
    list1[i]=list1[i].split()

for i in range(10):
    for i2 in range(10):
        length=len(list1[i][i2])
        try:
            if list1[i][i2+1]!=2 or list1[i][i2+1]!=1:
                null=""
        except:
            null=""
print(list1)

