import random
seq = []
strnum = ''
for i in range(1000):
    seq.append(str(i))
n = eval(input("请输入一个整数:"))
random.seed(n)
for i in range(10):
    strnum += random.choice(seq)
print(strnum)
