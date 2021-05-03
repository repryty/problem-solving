lines = ""
for i in range(2):
    lines+=input()+"\n"

lines=lines.strip()
    

day=lines.split()[0]
day=int(day)
car=lines.split()

ancar=[]

for i in range(10):
    i+=1
    car[i]=int(car[i])

if day%2==0: #짝수
    for i in range(10):
        i+=1
        if car[i]%2==0: #짝수
            ancar.append(car[i])

if day%2!=0: #홀수
    for i in range(10):
        i+=1
        if car[i]%2!=0: #홀수
            ancar.append(car[i])

print(len(ancar))