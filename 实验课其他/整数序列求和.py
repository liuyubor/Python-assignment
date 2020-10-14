
N = eval(input('请输入一个整数:'))
value = 0
for i in range(N+1):
    value += i
print('序列求和结果为：{:d}'.format(value))
