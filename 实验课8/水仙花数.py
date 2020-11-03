from random import random
strnum = ""
for i in range(100, 1000):
    a = pow(i//100, 3)
    b = pow(i % 100//10, 3)
    c = pow(i % 10, 3)
    if str(a)+str(b)+str(c) == str(i):
        strnum += ',' + str(i)
print(strnum)
