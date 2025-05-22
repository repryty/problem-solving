import sys

inp=[]
def round(inp: float):
    if inp - int(inp) >= 0.5:
        return int(inp)+1
    else:
        return int(inp)
        
for i in range(int(sys.stdin.readline())):
    inp.append(int(sys.stdin.readline()))
inp.sort()
fornum=range(round(len(inp)*0.15))
for i in fornum:
    inp.pop()
inp.reverse()
for i in fornum:
    inp.pop()
if len(inp)==0:
    print(0)
else:
    
    sys.stdout.write(str(round(sum(inp)/len(inp))))