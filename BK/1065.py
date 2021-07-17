inp=int(input)
def hansu(input):
    su=[]
    input=str(input)
    input=list(input)
    for i in range(len(input)):
        su.append(input[int(i)]-input(int(i)+1))
    for i in range(len(input)): 
        su