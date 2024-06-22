a,b,c=list(map(int, input().split()))
def kids(n):
    if n>=10:
        return (n*500)/100*90
    else:
        return n*500
def teen(n):
    if n>=15:
        return (n*800)/100*85
    else:
        return n*800
def adult(n):
    return n*1000
print(int(kids(a)+teen(b)+adult(c)))