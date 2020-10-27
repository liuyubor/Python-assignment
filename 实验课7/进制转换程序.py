
x = int(input("请输入待转换的整数："))
r = int(input("请输入转换的进制数（r>=2）："))
result = ''
while x != 0:
    num = x % r
    x //= r
    if num > 9:
        result += chr(num+55)
    else:
        result += str(num)

print(result[::-1])
