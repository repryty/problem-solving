inp=input()
inp2=[]
for i in inp:
    inp2.append(input())

def fibonacci(n):
    if n==0:
        print(0)
    elif n==1:
        print(1)
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(30))