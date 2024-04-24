
for i in range(int(input())):
    inp=[int(i) for i in input().split()]
    env=dict()
    for i in inp:
        if env.get(i)==None:
            env[i]=1
        else:
            env[i]+=1
    env=sorted(env.items(), key=lambda x: x[1], reverse=True)
    # print(env)
    if sum(dict(env).values())/2<=env[0][1]: print(env[0][0])
    else: print("SYJKGW")