import time

s = input('请输入：')
x = s.split(',')
t1 = time.strptime(x[0], '%Y年%m月%d日%H点%M分%S秒')
t2 = time.strptime(x[1], '%Y年%m月%d日%H点%M分%S秒')
print(t2.tm_yday-t1.tm_yday)
