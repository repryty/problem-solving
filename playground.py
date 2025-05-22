import random
N = random.randint(3, 1000)
print(N)
for _ in range(N):
    print(" ".join([str(random.randint(1, 9)) for _ in range(5)]))