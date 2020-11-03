import random
random.seed(17)
n = eval(input())
for i in range(3):
    s = random.randint(pow(10, n-1), int('9'*n))
    print(s)
