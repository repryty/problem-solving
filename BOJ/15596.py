def solve(a: list):
    map(int, a)
    end=0
    for i in range(len(a)):
        end+=a[i]
    return end

    