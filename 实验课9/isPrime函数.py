
def isPrime(a):
    try:
        a = eval(a)
        for i in range(1, a+1):
            if (a % i == 0) and (i != 1 and a != i):
                return False
            else:
                continue
        return True
    except TypeError:
        print("输入错误！请输入一个整数")


num = input("请输入一个整数：")
if isPrime(num):
    print("是质数！")
else:
    print("不是质数！")
