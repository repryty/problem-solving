lines = ""
for i in range(2):
    lines+=input()+"\n"
lines=lines.split()

for i in range(4):
    lines[i]=int(lines[i])

time1=(lines[0]*60)+lines[1]
time2=lines[2]+lines[3]

time3=time1-time2

h=int(time3/60)
m=time3-h*60

print(str(h)+" "+str(m))
