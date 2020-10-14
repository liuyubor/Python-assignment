# daydayup 3.0

def dayup(d, value):
    dayfactor = 0.01
    for i in range(d):
        if i % 7 in [4, 5, 6, 0]:
            value *= (1+dayfactor)
    return value

worktime = eval(input('请输入休息周期：'))
day, value = 365, 1
while (day != 2 and day != 13):
    value = dayup(worktime, value)
    day -= worktime + 1
print('每{:d}天最后的能力值为：{:.2f}'.format(worktime, value))
