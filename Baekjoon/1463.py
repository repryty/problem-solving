inp=int(input())

dp=dict()

def ps(inpu):
    if dp.get(inpu)==None:
        print(inpu)
        if inpu%3==0:
            dp[inpu]==inpu//3
            ps(inpu//3)
        elif inpu%2==0:
            ps(inpu//2)
        else:
            ps(inpu-1)
