# 快乐数字

n = eval(input('输入一个数字：'))

def operation(n):
    value = 0
    for i in range(len(str(n))):
        value += (int(str(n)[i])**2)
    return value

while(n != 1 and n != 4):
    n = operation(n)
if(n == 1):
    print('Ture')
else:
    print('False')
