inp = [0,0,0]
for i in range(3):
    inp[i] = [int(i) for i in input().split()]

ga_sung_bi = []

for i in range(3): 
    money = inp[i][0]
    if money >= 500:
        ga_sung_bi.append(inp[i][1]/(money-50))
    else:
        ga_sung_bi.append(inp[i][1]/money)
# print(ga_sung_bi)
best = ga_sung_bi.index(max(ga_sung_bi))
if best == 0:
    print("S")
elif best == 1:
    print("N")
elif best == 2:
    print("U")