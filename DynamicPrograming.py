## 팩토리얼 ##
"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))
"""

### 피보나치 수열 ###
def fibonacci(n):
    if n==1:
        return 1
    else:
        print(n)
        return n+fibonacci(n-1)

print(fibonacci(5))