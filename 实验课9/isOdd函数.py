
def isOdd(a):
    if a % 2 == 0:
        return False
    else:
        return True


s = eval(input("请输入一个整数："))
print(isOdd(s))
