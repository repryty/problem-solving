N, M = [int(i) for i in input().split()]

mon_id = dict()
mon_name = dict()

for i in range(N):
    name = input()
    mon_id[i+1] = name
    mon_name[name] = i+1

keys = mon_name.keys()
for _ in range(M):
    i = input()
    if i in keys:
        print(mon_name[i])
    else:
        print(mon_id[int(i)])