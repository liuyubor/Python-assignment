def yue(a, b):
    while True:
        if a > b:
            num = a % b
            a, b = b, num
            if num == 0:
                return(a)
        else:
            a, b = b, a

a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
x = yue(a, b)
print("最大公约数为{}，最小公倍数为{}".format(x, a*b/x))
