def fib(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else: 
    nfib=fib(n-1)+fib(n-2)
    return nfib

n=int(input())
print(fib(n))  