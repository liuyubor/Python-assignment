def multi(x):
    n = 1
    for i in x:
        n *= int(i)
    return n


x = input("请输入若干整数：").split()
print(multi(x))
