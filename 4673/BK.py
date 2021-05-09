def d(n):
    end=0
    str1=str(n)
    for i in range(len(str1)):
        end+=int(str1[i])
    return end+int(n)

list1=range(10000)
for i in list1:
    