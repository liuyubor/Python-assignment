
x = input("请输入待转换的整数：")
r = input("请输入转换的进制数（r>=2）：")
result = ''
if x or r == "q":
    pass
else:
    while x != 0:
        x=int(x)
        r=int(r)
        num = x % r
        x //= r
        if num > 9:
            result += chr(num+55)
        else:
            result += str(num)
    print(result[::-1])
