def mn(inp):
    a,b = map(int, inp.split())
    if a>b:
        return b
    else:
        return a
def mx(inp):
    a,b = map(int, inp.split())
    if a>b:
        return a
    else:
        return b