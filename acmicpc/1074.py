N, R, C = [int(i) for i in input().split()]

def finding_z(n:int, r:int, c:int, counter: int=0):
    HALF=2**(n-1)
    if n == 1:
        counter += 2*r
        counter += c
        print(counter)
    elif HALF-1>=r and HALF-1>=c:
        finding_z(n-1, r, c, counter)
    elif HALF-1<r and HALF-1>=c:
        counter+=2*(HALF**2)
        finding_z(n-1, r-HALF, c, counter)
    elif HALF-1>=r and HALF-1<c:
        counter+=HALF**2
        finding_z(n-1, r, c-HALF, counter)
    elif HALF-1<r and HALF-1<c:
        counter+=3*HALF**2
        finding_z(n-1, r-HALF, c-HALF, counter)

finding_z(N, R, C)