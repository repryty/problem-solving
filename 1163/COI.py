lines=""
howmuchlines=int(input())
for i in range(howmuchlines):
    lines.strip()
    a=input()
    lines+=a+"\n"

lines=lines.split()

wina=0
winb=0

for i in range(2):
    if lines[i]=="A":
        wina+=1
    
    if lines[i]=="B": 
        winb+=1

if wina>winb:
    print("1A")

if wina<winb:
    print("1B")