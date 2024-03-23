inp=dict()
for i in range(int(input())):
    age, name=input().split()
    age=int(age)
    if inp.get(age)==None:
        inp[age]=[name]
    else:
        inp[age].append(name)

inp=dict(sorted(inp.items()))
for i in inp.keys():
    for ii in inp[i]:
        print(i, ii)