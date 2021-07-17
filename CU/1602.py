def getgdg(inp):
    inp=str(inp)
    if "." in inp:
        inp=inp.replace("-", "")
        inp=str("%.10g" %(float(inp)))
    else:
        inp=inp.replace("-", "")
    return inp
print(getgdg(input()))

