N, K=map(int, input().split())

def factorial(inp):
    if inp==0:
        return 1
    elif inp<3:
        return inp
    else:
        return inp*factorial(inp-1)
    
# print(factorial(K))
print(factorial(N)//(factorial(K)*factorial(N-K)))
