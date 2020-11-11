def isNum(num):
    try:
        n = type(eval(num))
        if n == type(1):
            return True
        elif n == type(1.0):
            return True
        elif n == type(1+1j):
            return True
    except:
        return False


n = input("请输入一个字符串：")
print(isNum(n))
