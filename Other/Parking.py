inp=int(input())
lit=inp
def getP(f):
    if f%2!=0 or f%3!=0:
        lit-=1
        getP(lit)
    else:
        